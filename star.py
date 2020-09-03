import pygame as pg
from Pylaga.constants import DISPLAY_WIDTH
from random import randrange


class Star(pg.sprite.Sprite):
    def __init__(self):
        super(Star, self).__init__()

        self.wid = randrange(1, 4)
        self.hei = self.wid
        self.size = (self.wid, self.hei)
        self.image = pg.Surface(self.size)
        self.rect = self.image.get_rect()
        self.rect.x = randrange(0, DISPLAY_WIDTH)
        self.color = (randrange(0, 255), randrange(0, 255), randrange(0, 255))
        self.image.fill(self.color)
        self.spd_y = randrange(4, 20)

    def update(self):
        self.rect.y += self.spd_y
