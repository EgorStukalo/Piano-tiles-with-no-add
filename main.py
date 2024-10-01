import time
import tiles as t
import pygame.event
import images
import settings as s
import pygame as pg
import random
import pygame.freetype
pg.init()
pg.mixer.init()
import menu

class Game_is_game:
    def __init__(self):
        self.window = pg.display.set_mode(s.SIZE)
        self.true_false = True
        self.fps = pygame.time.Clock()
        self.tile_creation = pygame.USEREVENT
        pygame.time.set_timer(self.tile_creation, 500)
        self.tile_list = []
        self.tile_number = 0
        self.score_text = pg.freetype.Font("BodoniFLF-Roman.ttf", 30)
        self.score = 0
        self.song_duration = s.MORNING_DURATION
        self.song_notes = s.MORNING_NOTES
        self.hp = 3
        self.menu = menu.Menu(self)
        self.mode = 1
    def event(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.true_false = False
            if event.type == self.tile_creation and self.tile_number < len(self.song_notes):
                tile = t.Tile(self.song_duration[self.tile_number],self.song_notes[self.tile_number],self)
                if tile.length == 2:
                    pygame.time.set_timer(self.tile_creation, 999)
                else:
                    pygame.time.set_timer(self.tile_creation, 500)
                self.tile_number += 1
                self.tile_list.append(tile)
            if event.type == pg.MOUSEBUTTONDOWN:
                for tile in self.tile_list:
                    if tile.hitbox.collidepoint(event.pos) == True and tile.pressed == False:
                        tile.click()
                        for pressing_tile in self.tile_list:
                            if pressing_tile.hitbox.y > tile.hitbox.y and pressing_tile.pressed == False:
                                self.hp -= 1

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if self.score >= len(self.song_notes)- 3 or self.hp <= 0:
                        self.mode = 1
    def drawing(self):
        a = 0
        self.window.fill([255,255,255])
        while a <= s.NUMBEROFLINES:
            pg.draw.line(self.window,[0,0,0],[s.LINEWIDTH*a,0],[s.LINEWIDTH*a,s.SIZE[1]])
            a += 1
        if self.hp> 0:
            for tile in self.tile_list:
                tile.drawing(self.window)
        self.score_text.render_to(self.window, [20, 500],
                                  "you scored "+str(self.score)+" out of "+str(len(self.song_notes)), [0, 0, 0])
        self.score_text.render_to(self.window, [20, 450],
                                  "hp="+str(self.hp), [0, 0, 0])
        if self.score >= len(self.song_notes)- (3-self.hp):
            self.score_text.render_to(self.window, [20, 250],"Stand proud. You're strong.",[0, 0, 0])
        if self.hp <= 0:
            self.score_text.render_to(self.window, [20, 250], "You are a failure", [0, 0, 0])

        pg.display.update()
    def update(self):
        if self.hp > 0:
            for tile in self.tile_list:
                tile.falling()
                if tile.hitbox.y == 600 and tile.pressed == False:
                    self.hp -= 1
                    self.tile_list.remove(tile)
    def start(self):
        while self.true_false:
            if self.mode == 0:
                self.event()
                self.drawing()
                self.update()

            else:
                self.menu.event()
                self.menu.drawing()
                self.menu.update()
            self.fps.tick(100)
game = Game_is_game()
game.start()
            




