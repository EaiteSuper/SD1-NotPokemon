import pygame
import sys

# Constants
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 50
FPS = 60
MOVEMENT_DELAY = 100  # Increase this value to slow down the player

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

# Player position
player_pos = [0, 0]

# Movement flags
moving_up = False
moving_down = False
moving_left = False
moving_right = False

# Movement timer
movement_timer = 0

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moving_up = True
            elif event.key == pygame.K_DOWN:
                moving_down = True
            elif event.key == pygame.K_LEFT:
                moving_left = True
            elif event.key == pygame.K_RIGHT:
                moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                moving_up = False
            elif event.key == pygame.K_DOWN:
                moving_down = False
            elif event.key == pygame.K_LEFT:
                moving_left = False
            elif event.key == pygame.K_RIGHT:
                moving_right = False

    # Update player position
    if pygame.time.get_ticks() - movement_timer > MOVEMENT_DELAY:
        if moving_up and player_pos[1] > 0 and map_data[player_pos[1] - 1][player_pos[0]] == 0:
            player_pos[1] -= 1
        if moving_down and player_pos[1] < len(map_data) - 1 and map_data[player_pos[1] + 1][player_pos[0]] == 0:
            player_pos[1] += 1
        if moving_left and player_pos[0] > 0 and map_data[player_pos[1]][player_pos[0] - 1] == 0:
            player_pos[0] -= 1
        if moving_right and player_pos[0] < len(map_data[0]) - 1 and map_data[player_pos[1]][player_pos[0] + 1] == 0:
            player_pos[0] += 1
        movement_timer = pygame.time.get_ticks()

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
