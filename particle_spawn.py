import pygame as pg
from Pylaga.paticle import Particle
from random import randrange


class ParticleSpawn:
    def __init__(self):
        self.particle_gp = pg.sprite.Group()

    def particle_spawn(self, pos):
        random_number = randrange(3, 30)

        for num_part in range(random_number):
            new_particle = Particle()
            new_particle.rect.x = pos[0]
            new_particle.rect.y = pos[1]
            self.particle_gp.add(new_particle)

    def update(self):
        self.particle_gp.update()
