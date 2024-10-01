import pygame as pg
import pygame.transform
import settings as s
import random

def load_image_U_transorm_scale(file_name,x_dimension,y_dimension):
    return pygame.transform.scale(pg.image.load(file_name),[x_dimension,y_dimension])

long_tile = load_image_U_transorm_scale("long_tile.png",s.LINEWIDTH,300)
long_tile_pressed = load_image_U_transorm_scale("long_tile_pressed.png",s.LINEWIDTH,300)
short_tile = load_image_U_transorm_scale("short_tile.png",s.LINEWIDTH,150)
short_tile_pressed = load_image_U_transorm_scale("short_tile_pressed.png",s.LINEWIDTH,150)
menu_image = load_image_U_transorm_scale("menu.png",s.SIZE[0],s.SIZE[1])



