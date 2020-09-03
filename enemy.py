import pygame as pg
from Pylaga.constants import DISPLAY_WIDTH
from random import randrange


class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()

        self.image = pg.image.load('assets/images/sprites/Enemy.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (self.image.get_width() * 2,
                                                     self.image.get_height() * 2))
        self.rect = self.image.get_rect()
        self.rect.x = randrange(0, DISPLAY_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.hp = 2
        self.point = 1
        self.spd_y = randrange(3, 6)
        self.bullet = pg.sprite.Group()
        self.snd_hited = pg.mixer.Sound('assets/sounds/sound_effects/Hit.ogg')

    def hit(self):
        self.snd_hited.play()
        self.hp -= 1

        if self.hp <= 0:
            self.death()

    def death(self):
        self.point += 3
        self.kill()

    def update(self):
        self.rect.y += self.spd_y
