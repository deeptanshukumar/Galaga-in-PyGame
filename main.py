import pygame as pg
from Pylaga.constants import DISPLAY_SIZE
from Pylaga.background import BackGround
from Pylaga.ship import Ship
from Pylaga.enemy_spawn import EnemySpawn
from Pylaga.particle_spawn import ParticleSpawn
from Pylaga.event import Event

pg.mixer.init(44100, -16, 2, 512)

'DISPLAY'
display = pg.display.set_mode(DISPLAY_SIZE)

'FPS'
clock = pg.time.Clock()
fps = 60

'OBJECTS'
event = Event()
bg = BackGround()
bg_gp = pg.sprite.Group()
bg_gp.add(bg)
ship = Ship()
ship_gp = pg.sprite.Group()
ship_gp.add(ship)
enemy_spawn = EnemySpawn()
particle_spawn = ParticleSpawn()

'MUSIC'
pg.mixer.music.load('assets/sounds/music/Interstellar.ogg')
pg.mixer.music.set_volume(0.7)
pg.mixer.music.play(-1)

'LOOP'
running = True
while running:
    clock.tick(fps)

    'EVENT'
    event.events(ship)

    'OBJECT UPDATE'
    bg_gp.update()
    ship_gp.update()
    enemy_spawn.update()
    particle_spawn.update()

    'COLLISION'
    collision = pg.sprite.groupcollide(ship.bullet, enemy_spawn.enemy_gp, True, False)
    for bullet, enemy in collision.items():
        enemy[0].hit()
        ship.hud.score.update_score(enemy[0].point)
        particle_spawn.particle_spawn((bullet.rect.x, bullet.rect.y))
    collision = pg.sprite.groupcollide(ship_gp, enemy_spawn.enemy_gp, False, False)
    for ship, enemy in collision.items():
        if enemy[0] and not ship.is_invincible:
            ship.hit()
            enemy[0].hp = 0
            enemy[0].hit()
    for enemy in enemy_spawn.enemy_gp:
        collision = pg.sprite.groupcollide(ship_gp, enemy.bullet, False, True)
        for ship, bullet in collision.items():
            if not ship.is_invincible:
                ship.hit()

    'DISPLAY RENDER'
    bg_gp.draw(display)
    ship_gp.draw(display)
    ship.bullet.draw(display)
    enemy_spawn.enemy_gp.draw(display)
    for enemy in enemy_spawn.enemy_gp:
        enemy.bullet.draw(display)
    particle_spawn.particle_gp.draw(display)
    ship.hud_gp.draw(display)
    ship.hud.health_bar_gp.draw(display)
    ship.hud.icon_gp.draw(display)
    ship.hud.score_gp.draw(display)

    pg.display.update()
