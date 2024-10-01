import pygame as pg
import pygame.transform
import settings as s
import random
import images as i
class Tile():
    def __init__(self, length, name, game):
        self.game = game
        self.length = length
        if length == 1:
            self.image = i.short_tile
            self.frames_needed= 1
        else:
            self.image = i.long_tile
            self.frames_needed = 23
        self.frames_pressed = 0
        x = self.image.get_width()
        y = self.image.get_height()
        self.hitbox = pygame.rect.Rect([random.randint(0,3)*s.LINEWIDTH,-100],[x,y])
        self.speedy = 5
        self.sound = pygame.mixer.Sound("Sounds/"+name+".ogg")
        self.pressed = False
        self.truly_pressed = False
    def drawing(self, window):
        window.blit(self.image, self.hitbox)
    def falling(self):
        self.hitbox.y += self.speedy
        mouse_pressed = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        if self.pressed == True and mouse_pressed[0]==True and self.hitbox.collidepoint(mouse_pos) and self.truly_pressed == False:
            self.frames_pressed += 1
            a = random.randint(0,1)
            if self.length == 2:
                if a == 0:
                    self.image = i.long_tile
                if a == 1:
                    self.image = i.long_tile_pressed
            if self.frames_pressed == self.frames_needed:
                self.truly_pressed = True
                if self.length == 1:
                    self.image = i.short_tile_pressed
                else:
                    self.image = i.long_tile_pressed
                self.game.score += 1
    def click(self):
        if pygame.mixer.find_channel() == None:
            pygame.mixer.stop()
            self.sound.play()
        else:
            self.sound.play()
        self.pressed = True