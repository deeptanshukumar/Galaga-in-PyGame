import pygame as pg
from Pylaga.constants import DISPLAY_WIDTH, DISPLAY_HEIGHT, white

pg.font.init()


class Score(pg.sprite.Sprite):
    def __init__(self):
        super(Score, self).__init__()

        self.score = 0
        self.font_size = 15
        self.color = white
        self.font = pg.font.Font(None, self.font_size)
        self.image = self.font.render(str(f'Score: {self.score}'), True, self.color, None)
        self.rect = self.image.get_rect()
        self.rect.x = DISPLAY_WIDTH - self.rect.width - 7
        self.rect.y = DISPLAY_HEIGHT - self.rect.height - 9

    def update_score(self, point):
        self.score += point
        self.image = self.font.render(str(f'Score: {self.score}'), True, self.color, None)
        self.rect = self.image.get_rect()
        self.rect.x = DISPLAY_WIDTH - self.rect.width - 7
        self.rect.y = DISPLAY_HEIGHT - self.rect.height - 9

    def update(self):
        pass
