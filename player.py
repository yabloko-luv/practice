import pygame as pg
from constant import WORLD_GRAVITY, SCREEN_W

class Player:
    def __init__(self, x, y, speed, jump_force):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.color = "green"
        self.speed = speed
        self.rect = pg.Rect(x, y, self.width, self.height)
        self.jump_force = jump_force
        self.on_ground = True
        self.y_velocity = 0
        self.max_fall_speed = 10 

    def move(self, keys, platforms=[],traps=[]):
        if keys[pg.K_a]:
            self.x -= self.speed
        if keys[pg.K_d]:
            self.x += self.speed
        if keys[pg.K_SPACE] and self.on_ground:
            self.y_velocity = -self.jump_force
            self.on_ground = False
        if not self.on_ground:
            self.y_velocity = min(self.y_velocity + WORLD_GRAVITY, self.max_fall_speed)
            self.y += self.y_velocity

        self.rect.x = self.x
        self.rect.y = self.y
        self.on_ground = False

        if self.x >= SCREEN_W - self.width:
            self.x = SCREEN_W - self.width
        if self.x <= 0:
            self.x = 0
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.y_velocity > 0 and self.rect.bottom > platform.rect.top:
                    self.y = platform.rect.top - self.height
                    self.on_ground = True
                    self.y_velocity = 0
                elif self.y_velocity < 0 and self.rect.top < platform.rect.bottom:
                    self.y = platform.rect.bottom
                    self.y_velocity = 0

        for trap in traps:
            trap.check_collision(self)

        self.rect.x = self.x
        self.rect.y = self.y
        
    def draw(self, screen):
        pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))