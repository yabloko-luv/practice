import pygame as pg
class Button:
    def __init__(self, x, y, width, height, text, action=None):
        self.rect = pg.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.is_hovered = False
    
    def draw(self, surface):
        color = (100, 200, 100) if self.is_hovered else (70, 150, 70)
        pg.draw.rect(surface, color, self.rect, border_radius=10)
        pg.draw.rect(surface, (200, 200, 200), self.rect, 2, border_radius=10)
        
        font = pg.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
    
    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)
        return self.is_hovered
    
    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            return self.action
        return None