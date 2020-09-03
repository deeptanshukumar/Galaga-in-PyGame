import pygame as pg
from Pylaga.constants import DISPLAY_WIDTH
from Pylaga.bullet import Bullet
from random import randrange


class EnemyShip(pg.sprite.Sprite):
    def __init__(self):
        super(EnemyShip, self).__init__()

        self.image = pg.image.load('assets/images/sprites/Enemy_Ship.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (self.image.get_width() * 2,
                                                     self.image.get_height() * 2))
        self.rect = self.image.get_rect()
        self.rect.x = randrange(0, DISPLAY_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.hp = 3
        self.bullet = pg.sprite.Group()
        self.bullet_max_time = 60
        self.bullet_time = self.bullet_max_time
        self.states = {'Down': 'Down',
                       'Attack': 'Attack'}
        self.state = self.states['Down']
        self.point = 2
        self.spd_x = 0
        self.spd_y = randrange(3, 4)
        self.snd_hited = pg.mixer.Sound('assets/sounds/sound_effects/Hit.ogg')

    def state_down(self):

        if self.rect.y >= 100:
            self.state = self.states['Attack']

    def state_attack(self):
        self.spd_y = 0

        while self.spd_x == 0:
            self.spd_x = randrange(-4, 4)

        if self.bullet_time == 0:
            self.shoot()
            self.bullet_time = self.bullet_max_time
        else:
            self.bullet_time -= 1

        if self.rect.x <= 0:
            self.spd_x *= -1
        elif self.rect.x + self.rect.width >= DISPLAY_WIDTH:
            self.spd_x *= -1

    def shoot(self):
        new_bullet = Bullet()
        new_bullet.spd_y = 4
        new_bullet.rect.x = self.rect.x + (self.rect.width // 2) - 2
        new_bullet.rect.y = self.rect.y + self.rect.height + 1
        self.bullet.add(new_bullet)

    def hit(self):
        self.snd_hited.play()
        self.hp -= 1

        if self.hp <= 0:
            self.death()

    def death(self):
        self.point += 4
        self.kill()

    def update(self):
        self.bullet.update()
        if self.state == 'Down':
            self.state_down()
        elif self.state == 'Attack':
            self.state_attack()

        self.rect.x += self.spd_x
        self.rect.y += self.spd_y
