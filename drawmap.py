import pygame

class MapData:
     

def drawmap(MapData map):
    for y, row in enumerate(map):
            for x, tile in enumerate(row):
                if tile == 1:
                    pygame.draw.rect(screen, BLACK, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
