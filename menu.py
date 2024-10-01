import pygame as pg
import images
import settings as s

class Menu():
    def __init__(self,game):
        self.game = game
        self.V_lesu_rodilas_yolochka_color = [255,255,255]
        self.Berezka_color = [0,0,0]
        self.Utro_color = [0,0,0]
        self.chosen_song_number = 1
    def event(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.game.true_false = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    if self.chosen_song_number == 1:
                        self.chosen_song_number = 2
                        self.V_lesu_rodilas_yolochka_color = [0,0,0]
                        self.Berezka_color = [255,255,255]
                    elif self.chosen_song_number == 2:
                        self.chosen_song_number = 3
                        self.Berezka_color = [0, 0, 0]
                        self.Utro_color = [255, 255, 255]
                if event.key == pg.K_UP:
                    if self.chosen_song_number == 2:
                        self.chosen_song_number = 1
                        self.V_lesu_rodilas_yolochka_color = [255,255,255]
                        self.Berezka_color = [0,0,0]
                    elif self.chosen_song_number == 3:
                        self.chosen_song_number = 2
                        self.Berezka_color = [255, 255, 255]
                        self.Utro_color = [0, 0, 0]
                if event.key == pg.K_RETURN:
                    self.game.mode = 0
                    self.game.song_notes = s.song_notes[self.chosen_song_number]
                    self.game.song_duration = s.song_duration[self.chosen_song_number]
                    self.game.score = 0
                    self.game.hp = 3
                    self.game.tile_number = 0
                    self.game.tile_list = []

    def drawing(self):
        self.game.window.blit(images.menu_image,[0,0])
        self.game.score_text.render_to(self.game.window, [20, 150], "V lesu rodilas yolochka", self.V_lesu_rodilas_yolochka_color)
        self.game.score_text.render_to(self.game.window, [20, 250], "Berezka", self.Berezka_color)
        self.game.score_text.render_to(self.game.window, [20, 350], "Utro", self.Utro_color)
        pg.display.update()
    def update(self):
        pass

