import pygame as pg
from constant import *

class Trap:
    def __init__(self, x, y, width, height, start_x=200, start_y=GROUND,
                 has_text=False, text="", text_x=None, text_y=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = "red"
        self.rect = pg.Rect(x, y, width, height)
        self.start_x = start_x
        self.start_y = start_y
        self.has_text = has_text
        self.text = text
        self.show_text = False
        self.text_timer = 0

        self.text_x = text_x if text_x is not None else self.rect.x
        self.text_y = text_y if text_y is not None else self.rect.y - 30
    
    def check_collision(self, player):
        if self.rect.colliderect(player.rect):
            player.x = self.start_x
            player.y = self.start_y
            player.rect.x = player.x
            player.rect.y = player.y
            player.on_ground = True
            player.y_velocity = 0
            
            if self.has_text:
                self.show_text = True
                self.text_timer = 500
            death_event = pg.event.Event(pg.USEREVENT + 1)
            pg.event.post(death_event)
            
            return True
        return False
    
    def update_text(self):
        if self.show_text:
            self.text_timer -= 1
            if self.text_timer <= 0:
                self.show_text = False
    
    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)
        
        if self.show_text:
            font = pg.font.SysFont(None, 36)
            text_surface = font.render(self.text, True, (0, 0, 0))
            screen.blit(text_surface, (self.text_x, self.text_y))