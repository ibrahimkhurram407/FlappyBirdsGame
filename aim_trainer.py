import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Game settings
WIDTH = 800
HEIGHT = 600
TARGET_SIZE = 50
TARGET_COLORS = [(255, 0, 0), (0, 0, 255), (0, 255, 0)]
TARGET_SPEEDS = [10, 8, 5]

# Colors
BLACK = (0, 0, 0)

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Target Shooting Game")
clock = pygame.time.Clock()

# Load font
font = pygame.font.Font(None, 36)

# Create targets list
targets = []

# Game loop
while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked_target = None
            for target in targets:
                if target["rect"].collidepoint(pygame.mouse.get_pos()):
                    clicked_target = target
                    break
            if clicked_target:
                targets.remove(clicked_target)

    # Generate new targets
    if random.randint(0, 100) < 3:
        color_idx = random.randint(0, len(TARGET_COLORS) - 1)
        color = TARGET_COLORS[color_idx]
        speed = TARGET_SPEEDS[color_idx]
        target_rect = pygame.Rect(random.randint(0, WIDTH - TARGET_SIZE), 0, TARGET_SIZE, TARGET_SIZE)
        targets.append({"rect": target_rect, "color": color, "speed": speed})

    # Move targets
    for target in targets:
        target["rect"].y += target["speed"]
        if target["rect"].bottom >= HEIGHT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(BLACK)

    # Draw targets
    for target in targets:
        pygame.draw.rect(screen, target["color"], target["rect"])

    # Update the display
    pygame.display.update()
    clock.tick(30)
