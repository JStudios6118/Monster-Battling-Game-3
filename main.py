import pygame
import random
import json
import sys

import map as maps

WIDTH = 416
HEIGHT = 352
FPS = 30

tPack = 'final_textures'

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Importing Textures

f = open("textures/"+tPack+"/pack.json", 'r')

try:
  data = json.load(f)
except:
  print("\nERROR: No pack.json file found while loading the texture pack! If this is your texture pack, please create a new pack.json file or make sure your pack.json file is inside the textures folder and not a sub folder.")
  sys.exit()

print("Texture pack loaded!")

print(f"Name: {data['name']}\nDescription: {data['description']}\nMade by {data['author']}")

player = pygame.image.load(f'textures/{tPack}/player/player_down.png')

grass = pygame.image.load(f'textures/{tPack}/terrain/grass.png')
stone = pygame.image.load(f'textures/{tPack}/terrain/stone.png')
water = pygame.image.load(f'textures/{tPack}/terrain/water.png')
shore_down = pygame.image.load(f'textures/{tPack}/terrain/shore_south.png')
tree = pygame.image.load(f'textures/{tPack}/terrain/tree.png')
portal = pygame.image.load(f'textures/{tPack}/terrain/portal.png')

grass = pygame.transform.scale(grass, (32, 32))

# Function to draw text on the screen
def text(msg, x, y, color, size, font): 
  try:
    fontobj = pygame.font.SysFont(font, size)
  except:
    fontobj = pygame.font.SysFont("freesans", 36)
  msgobj = fontobj.render(msg, False, color)
  screen.blit(msgobj,(x, y))

solid_blocks = [grass, stone, water]

map = []

terrain = [grass, grass, stone]
solids = [-1,1,6]


tileIDs = {
  -1:water,
  0:grass,
  1:stone,
  2:shore_down,
  6:tree,
  99:portal
}

for y in range(0,50):
  row = []
  for x in range(0,50):
    row.append(random.choice(terrain))
  map.append(row)

map = maps.scenes['dev']

#print(map[0][0])

##print(map)

## initialize pygame and create window
pygame.init()
#pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monster Battling Game 3")
clock = pygame.time.Clock()     ## For syncing the FPS

directions = {
  'up': (0,-1),
  'down': (0,1),
  'left': (-1,0),
  'right': (1,0),
  '':(0,0)
}

offset = [0,0]

player_x = 0
player_y = 0

SCROLL_TICK = -1
DIRECTION = ''

def playerCollisions(direction):
  global player_x, player_y, map
  
  direction=directions[direction]
  #print('dir:',direction)
  
  if player_x+direction[0]>=0 and player_y+direction[1]>=0:
    try:
      tile=map[player_y+direction[1]][player_x+direction[0]]
    except:
      return False
    else:
    
      if isinstance(tile, list):
        if tile[0] in solids:
          return False
        return True
      else:
        if tile in solids:
          return False
        return True
    return False
      

def scroll(direction):
  global offset
  global SCROLL_TICK
  global player_x
  global player_y
  global DIRECTION
  if (SCROLL_TICK!=-1):
    SCROLL_TICK+=1
    if (SCROLL_TICK!=17):
      if direction == 'up':
        offset[1]-=2
      if direction == 'down':
        offset[1]+=2
      if direction == 'left':
        offset[0]-=2
      if direction == 'right':
        offset[0]+=2
    else:
      SCROLL_TICK=-1
      player_x+=int(offset[0]/32)
      player_y+=int(offset[1]/32)
      offset = [0,0]
      #print(player_x, player_y)
      DIRECTION = ''


## Game loop



#13 x 11
#15 X 13 - y: 7 x: 6
running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if SCROLL_TICK == -1:
                if event.key == pygame.K_UP:
                    if playerCollisions('up'):
                      SCROLL_TICK=0
                      DIRECTION='up'
                if event.key == pygame.K_DOWN:
                    if playerCollisions('down'):
                      SCROLL_TICK=0
                      DIRECTION='down'
                if event.key == pygame.K_LEFT:
                    if playerCollisions('left'):
                      SCROLL_TICK=0
                      DIRECTION='left'
                if event.key == pygame.K_RIGHT:
                    if playerCollisions('right'):
                      SCROLL_TICK=0
                      DIRECTION='right'
                if event.key == pygame.K_p:
                    map = maps.scenes['dev2']
            ##print(directions[DIRECTION][0])
            try:
                #print(map[player_y-5][player_x-6])
                pass
            except:
                pass

    ##print(player_x,"and",y)
    scroll(DIRECTION)

    screen.fill(WHITE)

    #0,0 should be top left corner
    # Moving right shifts the map to left
    # Moving down shifts the map to up

    
    # screen drawing loops
    for y in range(-1, 12):
      for x in range(-1,14):
        # check if x or y is not in the tile list
        if player_x+x-6>=0 and player_y+y-5>=0:
          try:
            # get current tile data
            tile = map[player_y+y-5][player_x+x-6]
            if isinstance(tile, list):
              # draw tiles with extra properties
              screen.blit(tileIDs[tile[0]], (x*32-offset[0], y*32-offset[1]))
            else:
              # draw tiles with no properties
              screen.blit(tileIDs[tile], (x*32-offset[0], y*32-offset[1]))
              
          except:
            # draw water if indexerror
            screen.blit(water, (x*32-offset[0],y*32-offset[1]))
        else:
          # draw water if x or y is less than 0
          screen.blit(water, (x*32-offset[0],y*32-offset[1]))

    screen.blit(player, (192,160))
    text(f'({player_x}, {player_y})', 5, 5, BLACK, 14, 'freesans')
    text(f'{DIRECTION}', 50,5, BLACK, 15, 'freesans')
    #screen.blit(grass, (0,0))

    pygame.display.flip()   

pygame.quit()