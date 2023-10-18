import pygame
import random

import map

WIDTH = 416
HEIGHT = 352
FPS = 30



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

player = pygame.image.load('textures/player/player_down.png')

grass = pygame.image.load('textures/terrain/grass.png')
stone = pygame.image.load('textures/terrain/stone.png')
water = pygame.image.load('textures/terrain/water.png')

grass = pygame.transform.scale(grass, (32, 32))

solid_blocks = [grass, stone, water]

map = []

terrain = [grass, grass, stone]

for y in range(0,50):
  row = []
  for x in range(0,50):
    row.append(random.choice(terrain))
  map.append(row)

#print(map)

## initialize pygame and create window
pygame.init()
#pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monster Battling Game 3")
clock = pygame.time.Clock()     ## For syncing the FPS

player_x = 55
player_y = 54

## Game loop

#13 x 11
running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_y += 1
            if event.key == pygame.K_DOWN:
                player_y -= 1
            if event.key == pygame.K_LEFT:
                player_x += 1
            if event.key == pygame.K_RIGHT:
                player_x -= 1
            try:
                print(map[player_y-5][player_x-6])
            except:
                pass

    #print(player_x,"and",y)

    screen.fill(WHITE)

    for y in range(0,player_y+5):
        for x in range(0,player_x+6):
            
            try:
                screen.blit(map[player_y-y][player_x-x], (x*32, y*32))
            except:
                screen.blit(water, (x*32, y*32))

    screen.blit(player, (192,160))
    #screen.blit(grass, (0,0))
  
    pygame.display.flip()       

pygame.quit()