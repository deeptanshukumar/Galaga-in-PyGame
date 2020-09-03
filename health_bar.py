import pygame as pg


class HealthBar(pg.sprite.Sprite):
    def __init__(self, hp):
        super(HealthBar, self).__init__()

        self.max_hp = hp
        self.hp = self.max_hp
        self.orig_image = pg.image.load('assets/images/sprites/Health_Bar.png').convert()
        self.image = self.orig_image
        self.rect = self.image.get_rect()
        self.max_wid = self.image.get_width()
        self.spd_x = 0

    def decrease_hp(self):
        self.hp -= 1
        self.image = pg.transform.scale(self.orig_image, (self.max_wid * self.hp // self.max_hp,
                                                          self.rect.height))
        x = self.rect.x
        y = self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset_hp(self):
        self.hp = self.max_hp
        self.image = pg.transform.scale(self.orig_image, (self.max_wid * self.hp // self.max_hp,
                                                          self.rect.height))
        x = self.rect.x
        y = self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += self.spd_x
