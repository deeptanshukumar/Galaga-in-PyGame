import pygame as pg
from random import randrange


class Particle(pg.sprite.Sprite):
    def __init__(self):
        super(Particle, self).__init__()

        self.wid = randrange(1, 6)
        self.hei = self.wid
        self.size = (self.wid, self.hei)
        self.image = pg.Surface(self.size)
        self.rect = self.image.get_rect()
        self.color = (randrange(0, 255), randrange(0, 255), randrange(0, 255))
        self.image.fill(self.color)
        self.spd_x = randrange(-16, 16)
        self.spd_y = randrange(-16, 16)
        self.time = 60

    def update(self):
        self.rect.x += self.spd_x
        self.rect.y += self.spd_y

        if self.time == 0:
            self.kill()
        else:
            self.time -= 1
