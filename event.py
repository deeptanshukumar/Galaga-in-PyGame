import pygame as pg


class Event:
    def __init__(self):
        pass

    def events(self, ship):

        for event in pg.event.get():
            self.quit_event(event)
            self.keyboard_event(event, ship)

    def keyboard_event(self, event, ship):

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_d:
                ship.spd_x = ship.spd
            elif event.key == pg.K_a:
                ship.spd_x = -ship.spd
            if event.key == pg.K_SPACE:
                ship.shoot()
        if event.type == pg.KEYUP:
            if event.key == pg.K_d:
                ship.spd_x = 0
            elif event.key == pg.K_a:
                ship.spd_x = 0

    def quit_event(self, event):

        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            pg.quit()
            quit()
