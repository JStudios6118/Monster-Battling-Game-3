To create a tiled world map in Pygame, you can use the Tiled Map Editor to create a map from prepared tiles. You can specify the size of the map and tiles in Tiled, then export your map to a tmx format and load it to Python using pytmx ². 

Alternatively, you can create a tilemap in Pygame by creating a list of single tiles in the first layer of your game map. You can then display these tiles in locations using the `blit` method ¹. 

Here is an example code snippet that demonstrates how to display a tiled map in Pygame using Tiled and pytmx:

```python
import pygame
from pytmx import load_pygame

white = (255, 255, 255)
screenSize = (800, 600)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("GameName")
screen.fill(white)

gameMap = load_pygame("Frozen.tmx")

# Creates list of single tiles in first layer
images = []
for y in range(50):
    for x in range(50):
        image = gameMap.get_tile_image(x, y, 0)
        images.append(image)

# Displays tiles in locations
i = 0
for y in range(50):
    for x in range(50):
        screen.blit(images[i], (x * 32, y * 32))
        i += 1

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
```

I hope this helps!

Source: Conversation with Bing, 10/17/2023
(1) python - Tiled Map in Pygame - Stack Overflow. https://stackoverflow.com/questions/16599201/tiled-map-in-pygame.
(2) Is there an better way to create a tilemap in pygame?. https://stackoverflow.com/questions/54615257/is-there-an-better-way-to-create-a-tilemap-in-pygame.
(3) Creating Tilemaps in Pygame - 1.0. https://www.pygame.org/project/5291/7669.
(4) How do I display a tiled map in Pygame using Tiled and pytmx?. https://stackoverflow.com/questions/29053680/how-do-i-display-a-tiled-map-in-pygame-using-tiled-and-pytmx.