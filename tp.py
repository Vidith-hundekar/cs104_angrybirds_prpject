import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Angry Birds")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
background = pygame.image.load('./resources/images/background.png')
sling_image = pygame.image.load("resources/images/sling.png")
bird_image = pygame.image.load("resources/images/red.png")
target_image = pygame.image.load("resources/images/wood_100.png")

# Bird class
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bird_image
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = pygame.math.Vector2(0, 0)
        self.is_dragging = False
        self.initial_position = pygame.math.Vector2(x, y)

    def update(self):
        if not self.is_dragging:
            self.rect.center += self.velocity
            self.velocity.y += 0.5  # Gravity effect

            # Collision with ground
            if self.rect.bottom >= HEIGHT:
                self.rect.bottom = HEIGHT
                self.velocity.y *= -0.6  # Bounce effect

            # Collision with walls
            if self.rect.left <= 0 or self.rect.right >= WIDTH:
                self.velocity.x *= -0.6  # Bounce effect

    def start_drag(self, pos):
        self.is_dragging = True
        self.velocity = pygame.math.Vector2(0, 0)
        self.rect.center = pos

    def stop_drag(self, pos):
        self.is_dragging = False
        direction = self.initial_position - pygame.math.Vector2(pos)
        self.velocity = direction / 10  # Adjust speed factor

# Target class
class Target(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = target_image
        self.rect = self.image.get_rect(center=(x, y))

# Initialize game objects
bird = Bird(150, HEIGHT - 100)
target = Target(WIDTH - 150, HEIGHT - 100)
all_sprites = pygame.sprite.Group(bird, target)
targets = pygame.sprite.Group(target)

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)
    screen.blit(background, (0, 0))
    screen.blit(sling_image, (100, HEIGHT - 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if bird.rect.collidepoint(event.pos):
                bird.start_drag(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            bird.stop_drag(event.pos)

    if pygame.sprite.spritecollide(bird, targets, False):
        print("Hit!")
        running = False

    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
