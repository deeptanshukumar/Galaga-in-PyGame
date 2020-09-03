import pygame as pg
from Pylaga.constants import DISPLAY_HEIGHT
from Pylaga.enemy import Enemy
from Pylaga.enemy_ship import EnemyShip
from random import randrange


class EnemySpawn:
    def __init__(self):
        self.enemy_gp = pg.sprite.Group()
        self.spawn_time = randrange(30, 120)

    def enemy_spawn(self):
        random_number = randrange(0, 100)
        if random_number <= 80:
            new_enemy = Enemy()
        elif random_number >= 81:
            new_enemy = EnemyShip()

        self.enemy_gp.add(new_enemy)

    def update(self):
        self.enemy_gp.update()

        for enemy in self.enemy_gp:
            if enemy.rect.y >= DISPLAY_HEIGHT:
                self.enemy_gp.remove(enemy)

        if self.spawn_time == 0:
            self.enemy_spawn()
            self.spawn_time = randrange(30, 120)
        else:
            self.spawn_time -= 1
