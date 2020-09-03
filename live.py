import pygame as pg
from Pylaga.constants import white

pg.font.init()


class Lives(pg.sprite.Sprite):
    def __init__(self, num_lives):
        super(Lives, self).__init__()

        self.num_lives = num_lives
        self.wid = 35
        self.hei = 20
        self.size = (self.wid, self.hei)
        self.image = pg.Surface(self.size)
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.ship_img = pg.image.load('assets/images/sprites/Ship.png').convert()
        self.image.blit(self.ship_img, (0, 0))
        self.font_size = 15
        self.font = pg.font.Font(None, self.font_size)
        self.font_color = white
        self.lives_counter = self.font.render(f'x{self.num_lives}', True, self.font_color, False)
        self.image.blit(self.lives_counter, (20, 4))

    def decrement_life(self):
        self.num_lives -= 1

        if self.num_lives < 0:
            pg.quit()
            quit()
            self.num_lives = 0
        else:
            self.image = pg.Surface(self.size)
            self.image.set_colorkey((0, 0, 0))
            self.image.blit(self.ship_img, (0, 0))
            self.lives_counter = self.font.render(f'x{self.num_lives}', True, self.font_color, False)
            self.image.blit(self.lives_counter, (20, 4))

    def update(self):
        pass
