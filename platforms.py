import pygame as pg
class Platform:
    def __init__(self, x, y, width, height, color="blue"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pg.Rect(x, y, width, height)
    
    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)