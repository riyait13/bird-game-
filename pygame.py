import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Game settings
BIRD_WIDTH = 50
BIRD_HEIGHT = 35
PIPE_WIDTH = 70
PIPE_HEIGHT = 400
PIPE_GAP = 150
GRAVITY = 0.5
JUMP_STRENGTH = -10

# Load bird image
bird_image = pygame.transform.scale(pygame.image.load("bird.png"), (BIRD_WIDTH, BIRD_HEIGHT))

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bird Flying Game")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Bird class
class Bird:
    def __init__(self):
        self.x = 100
        self.y = SCREEN_HEIGHT // 2
        self.vel_y = 0

    def update(self):
        self.vel_y += GRAVITY
        self.y += self.vel_y

        if self.y > SCREEN_HEIGHT - BIRD_HEIGHT:
            self.y = SCREEN_HEIGHT - BIRD_HEIGHT
            self.vel_y = 0

    def jump(self):
        self.vel_y = JUMP_STRENGTH

    def draw(self):
        screen.blit(bird_image, (self.x, self.y))

# Pipe class
class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.height = random.randint(100, SCREEN_HEIGHT - PIPE_GAP - 100)
        
    def update(self):
        self.x -= 5

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, 0, PIPE_WIDTH, self.height))
        pygame.draw.rect(screen, GREEN, (self.x, self.height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT))

    def collide(self, bird):
        bird_rect = pygame.Rect(bird.x, bird.y, BIRD_WIDTH, BIRD_HEIGHT)
        top_pipe_rect = pygame.Rect(self.x, 0, PIPE_WIDTH, self.height)
        bottom_pipe_rect = pygame.Rect(self.x, self.height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT)
        return bird_rect.colliderect(top_pipe_rect) or bird_rect.colliderect(bottom_pipe_rect)

# Main game function
def game():
    bird = Bird()
    pipes = [Pipe()]
    score = 0
    running = True

    while running:
        clock.tick(60)
        screen.fill(BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        bird.update()
        bird.draw()

        if pipes[-1].x < SCREEN_WIDTH // 2:
            pipes.append(new_pipe)

        for pipe in pipes:
            pipe.update()
            pipe.draw()
            if pipe.collide(bird):
                running = False

        pipes = [pipe for pipe in pipes if pipe.x > -PIPE_WIDTH]

        score_text = pygame.font.SysFont(None, 36).render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    game()