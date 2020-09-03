import pygame as pg
from Pylaga.constants import DISPLAY_WIDTH, DISPLAY_HEIGHT
from Pylaga.bullet import Bullet
from Pylaga.hud import HUD


class Ship(pg.sprite.Sprite):
    def __init__(self):
        super(Ship, self).__init__()

        self.image = pg.image.load('assets/images/sprites/Ship.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (self.image.get_width() * 2,
                                                     self.image.get_height() * 2))
        self.rect = self.image.get_rect()
        self.rect.x = (DISPLAY_WIDTH // 2) - (self.rect.height // 2)
        self.rect.y = DISPLAY_HEIGHT - (self.rect.height * 2) - 5
        self.max_hp = 5
        self.hp = self.max_hp
        self.lives = 3
        self.is_invincible = False
        self.max_invincible_time = 60
        self.invincible_time = self.max_invincible_time
        self.bullet = pg.sprite.Group()
        self.snd_bullet = pg.mixer.Sound('assets/sounds/sound_effects/Shoot.ogg')
        self.snd_hited = pg.mixer.Sound('assets/sounds/sound_effects/Hit.ogg')
        self.spd = 6
        self.spd_x = 0
        self.hud = HUD(self.hp, self.lives)
        self.hud_gp = pg.sprite.Group()
        self.hud_gp.add(self.hud)

    def shoot(self):
        self.snd_bullet.play()
        new_bullet = Bullet()
        new_bullet.rect.x = self.rect.x + (self.rect.width // 2) - 2
        new_bullet.rect.y = self.rect.y - 1
        self.bullet.add(new_bullet)

    def hit(self):
        self.snd_hited.play()
        self.hp -= 1
        self.hud.health_bar.decrease_hp()

        if self.hp <= 0:
            self.hp = 0
            self.death()

    def death(self):
        self.hp = self.max_hp
        self.hud.health_bar.reset_hp()
        self.hud.lives.decrement_life()
        self.rect.x = (DISPLAY_WIDTH / 2) - (self.rect.height / 2)
        self.is_invincible = True
        self.invincible_time = self.max_invincible_time

    def update(self):
        self.bullet.update()
        self.hud_gp.update()
        self.rect.x += self.spd_x

        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= DISPLAY_WIDTH - self.rect.width:
            self.rect.x = DISPLAY_WIDTH - self.rect.width

        for bullet in self.bullet:
            if bullet.rect.y <= 0:
                self.bullet.remove(bullet)

        if self.invincible_time > 0:
            self.invincible_time -= 1
        else:
            self.is_invincible = False
