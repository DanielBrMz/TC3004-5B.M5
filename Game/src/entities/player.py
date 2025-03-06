import pygame
from bullet import Bullet

class Player:
    def __init__(self, x,y,sprite_path):
        self.x = x
        self.y = y
        self.sprite_path = pygame.image.load(sprite_path)
        self.speed =  5

    def shoot(self):
        return Bullet(self.x+20, self.y)


    def move(self, keys, width):
        if keys[pygame.K_LEFT] and self.x<0:
            self.x -= self.speed
        elif keys[pygame.K_RIGHT] and self.x<width-50:
            self.x += self.speed


    def draw(self, screen):
        screen.draw_image(self.sprite_path, (self.x, self.y))