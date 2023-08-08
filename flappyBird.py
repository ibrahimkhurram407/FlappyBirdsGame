import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Game settings
WIDTH = 1200
HEIGHT = 800
PLAYER_SIZE = 50
GRAVITY = 9
JUMP_STRENGTH = -80
PILLAR_WIDTH = 50
PILLAR_GAP = 250
PILLAR_SPEED = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Pillars")
clock = pygame.time.Clock()

# Load player icon
player_icon = pygame.image.load("player_icon.png")  # Replace with your icon path
player_icon = pygame.transform.scale(player_icon, (PLAYER_SIZE, PLAYER_SIZE))
player_rect = player_icon.get_rect(center=(WIDTH // 4, HEIGHT // 2))

# Create pillars
pillars = []
def create_pillar():
    pillar_height = random.randint(100, 400)
    top_pillar = pygame.Rect(WIDTH, 0, PILLAR_WIDTH, pillar_height)
    bottom_pillar = pygame.Rect(WIDTH, pillar_height + PILLAR_GAP, PILLAR_WIDTH, HEIGHT - (pillar_height + PILLAR_GAP))
    pillars.extend([top_pillar, bottom_pillar])

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player_rect.y += JUMP_STRENGTH

    # Apply gravity to player
    player_rect.y += GRAVITY

    # Move and remove pillars
    for pillar in pillars:
        pillar.x -= PILLAR_SPEED
        if pillar.right <= 0:
            pillars.remove(pillar)
    
    # Create new pillars
    if len(pillars) == 0 or pillars[-1].centerx < WIDTH - PILLAR_GAP:
        create_pillar()

    # Check collision with pillars
    for pillar in pillars:
        if pillar.colliderect(player_rect):
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(BLACK)

    # Draw player icon
    screen.blit(player_icon, player_rect)

    # Draw pillars
    for pillar in pillars:
        pygame.draw.rect(screen, WHITE, pillar)

    pygame.display.update()
    clock.tick(30)
