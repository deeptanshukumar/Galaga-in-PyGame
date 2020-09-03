import pygame as pg
from Pylaga.constants import DISPLAY_HEIGHT
from Pylaga.health_bar import HealthBar
from Pylaga.heart_icon import HeartIcon
from Pylaga.score import Score
from Pylaga.live import Lives


class HUD(pg.sprite.Sprite):
    def __init__(self, hp, num_lives):
        super(HUD, self).__init__()

        self.image = pg.image.load('assets/images/sprites/HUD.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = DISPLAY_HEIGHT - self.rect.height
        self.health_bar = HealthBar(hp)
        self.health_bar.rect.x = 23
        self.health_bar.rect.y = DISPLAY_HEIGHT - self.health_bar.rect.height - 12
        self.health_bar_gp = pg.sprite.Group()
        self.health_bar_gp.add(self.health_bar)
        self.heart_icon = HeartIcon()
        self.lives = Lives(num_lives)
        self.lives.rect.x = 225
        self.lives.rect.y = DISPLAY_HEIGHT - 24
        self.score = Score()
        self.score_gp = pg.sprite.Group()
        self.score_gp.add(self.score)
        self.icon_gp = pg.sprite.Group()
        self.icon_gp.add(self.heart_icon)
        self.icon_gp.add(self.lives)

    def update(self):
        self.health_bar_gp.update()
        self.icon_gp.update()
        self.score_gp.update()
