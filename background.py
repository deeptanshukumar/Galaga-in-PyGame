import pygame as pg
from Pylaga.constants import DISPLAY_HEIGHT, DISPLAY_SIZE
from Pylaga.star import Star
from random import randrange


class BackGround(pg.sprite.Sprite):
    def __init__(self):
        super(BackGround, self).__init__()

        self.image = pg.Surface(DISPLAY_SIZE)
        self.rect = self.image.get_rect()
        self.color = (0, 0, 15)
        self.star = pg.sprite.Group()
        self.time = randrange(1, 10)

    def update(self):
        self.star.update()

        for star in self.star:
            if star.rect.y >= DISPLAY_HEIGHT:
                self.star.remove(star)

        if self.time == 0:
            new_star = Star()
            self.star.add(new_star)
            self.time = randrange(1, 10)

        self.image.fill(self.color)
        self.star.draw(self.image)
        self.time -= 1
