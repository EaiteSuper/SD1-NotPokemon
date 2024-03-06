import pygame
import sys

# Constants
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 50
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Player
player_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
player_image.fill(GREEN)
player_rect = player_image.get_rect()

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Map
map_data = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

# Game loop
running = True
player_pos = [0, 0]  # Starting position of the player
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.key.get_pressed() == pygame.K_UP:
            if player_pos[1] > 0 and map_data[player_pos[1] - 1][player_pos[0]] == 0:
                player_pos[1] -= 1
        elif pygame.key.get_pressed() == pygame.K_DOWN:
            if player_pos[1] < len(map_data) - 1 and map_data[player_pos[1] + 1][player_pos[0]] == 0:
                player_pos[1] += 1
        elif pygame.key.get_pressed() == pygame.K_LEFT:
            if player_pos[0] > 0 and map_data[player_pos[1]][player_pos[0] - 1] == 0:
                player_pos[0] -= 1
        elif pygame.key.get_pressed() == pygame.K_RIGHT:
            if player_pos[0] < len(map_data[0]) - 1 and map_data[player_pos[1]][player_pos[0] + 1] == 0:
                player_pos[0] += 1

    # Draw map
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile == 1:
                pygame.draw.rect(screen, BLACK, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Draw player
    player_rect.topleft = (player_pos[0] * TILE_SIZE, player_pos[1] * TILE_SIZE)
    screen.blit(player_image, player_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()