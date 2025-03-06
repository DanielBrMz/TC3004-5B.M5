import pygame
import random

from src.builder.director import EnemyDirector
from src.builder.enemy_builder import EnemyBuilder
from src.core.config import Config
from src.entities.player import Player

pygame.init()

# Configuration
config = Config()
WIDTH, HEIGHT = config.get("WIDTH"), config.get("HEIGHT")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader")

#Jugador
player = Player(WIDTH//2 , HEIGHT - 80)

# Enemies
director = EnemyDirector()
builder = EnemyBuilder()

enemies = [
    director.construct_enemy(builder,"normal"),
    director.construct_enemy(builder, "fast"),
    director.construct_enemy(builder, "strong"),

]

bullet=[]
enemy_speed = 1
enemy_spawn_timer = 0

running = True

while running:
    pygame.time.delay(30)
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    