import pygame

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = pygame.image.load('bullet.png')
        self.speed = 10
        self.width = 5
        self.height = 10
        self.color = (255,0,0)

    def move(self):
        self.y -= self.speed

    def draw(self, screen):
        screen.draw.rect(screen, self.color , (self.x, self.y, self.width, self.height))
