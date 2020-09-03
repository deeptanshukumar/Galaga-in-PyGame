import pygame as pg
from Pylaga.constants import white


class Bullet(pg.sprite.Sprite):
    def __init__(self):
        super(Bullet, self).__init__()

        self.wid = 4
        self.hei = 6
        self.size = (self.wid, self.hei)
        self.image = pg.Surface(self.size)
        self.rect = self.image.get_rect()
        self.color = white
        self.image.fill(self.color)
        self.spd_y = -5

    def update(self):
        self.rect.y += self.spd_y
