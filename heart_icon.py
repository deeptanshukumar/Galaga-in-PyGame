import pygame as pg
from Pylaga.constants import DISPLAY_HEIGHT


class HeartIcon(pg.sprite.Sprite):
    def __init__(self):
        super(HeartIcon, self).__init__()

        self.anim_list = [pg.image.load('assets/images/sprites/Heart_1.png').convert_alpha(),
                          pg.image.load('assets/images/sprites/Heart_2.png').convert_alpha(),
                          pg.image.load('assets/images/sprites/Heart_3.png').convert_alpha(),
                          pg.image.load('assets/images/sprites/Heart_4.png').convert_alpha(),
                          pg.image.load('assets/images/sprites/Heart_5.png').convert_alpha()]
        self.anim_index = 0
        self.max_index = len(self.anim_list) - 1
        self.max_frame_duration = 7
        self.frame_duration = self.max_frame_duration
        self.image = self.anim_list[self.anim_index]
        self.rect = self.image.get_rect()
        self.rect.x = 7
        self.rect.y = DISPLAY_HEIGHT - self.rect.height - 7

    def update(self):

        if self.frame_duration == 0:
            self.anim_index += 1
            if self.anim_index > self.max_index:
                self.anim_index = 0
            self.image = self.anim_list[self.anim_index]
            self.frame_duration = self.max_frame_duration

        self.frame_duration -= 1
