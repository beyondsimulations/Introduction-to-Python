import pygame

# Initialize Pygame
pygame.init()
star_time = 0

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY_LIGHT = (200, 200, 200)
GRAY_DARK = (100, 100, 100)

# Player properties
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_SPEED = 5
JUMP_FORCE = -15
GRAVITY = 0.8

def show_game_over():
    font = pygame.font.Font(None, 74)
    text = font.render('Game Over', True, RED)
    text_rect = text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

    retry_font = pygame.font.Font(None, 36)
    retry_text = retry_font.render('Press SPACE to retry or Q to quit', True, WHITE)
    retry_rect = retry_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 50))

    screen.fill(BLACK)
    screen.blit(text, text_rect)
    screen.blit(retry_text, retry_rect)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                if event.key == pygame.K_q:
                    return False
    return False

def show_winner():
    font = pygame.font.Font(None, 74)
    text = font.render('You Win!', True, GREEN)
    text_rect = text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

    retry_font = pygame.font.Font(None, 36)
    retry_text = retry_font.render('Press SPACE to play again or Q to quit', True, WHITE)
    retry_rect = retry_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 50))

    screen.fill(BLACK)
    screen.blit(text, text_rect)
    screen.blit(retry_text, retry_rect)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                if event.key == pygame.K_q:
                    return False
    return False

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Create pixel art for player
        self.image = pygame.Surface([PLAYER_WIDTH, PLAYER_HEIGHT])
        self.image.fill(BLACK)
        self.facing_right = True

        # Add pixel art details
        pygame.draw.rect(self.image, WHITE, [8, 8, 24, 44])  # Body
        pygame.draw.rect(self.image, BLACK, [14, 15, 4, 4])  # Eye
        pygame.draw.rect(self.image, BLACK, [22, 15, 4, 4])  # Eye
        pygame.draw.rect(self.image, BLACK, [14, 25, 12, 2])  # Mouth

        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = WINDOW_HEIGHT - 100
        self.velocity_y = 0
        self.can_jump = True
        self.double_jump = True

    def update(self):
        # Gravity
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        # Check for ground collision
        if self.rect.bottom > WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT
            self.velocity_y = 0
            self.can_jump = True
            self.double_jump = True

        # Flip sprite based on direction
        if keys[pygame.K_LEFT]:
            self.facing_right = False
            self.image = pygame.transform.flip(self.image, True, False)
        if keys[pygame.K_RIGHT]:
            self.facing_right = True
            self.image = pygame.transform.flip(self.image, False, False)

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)

        # Add texture to platform
        for i in range(0, width, 4):
            pygame.draw.line(self.image, GRAY_LIGHT, (i, 0), (i, height), 1)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(BLACK)

        # Add pixel art details
        pygame.draw.rect(self.image, WHITE, [2, 2, 26, 26])  # Body
        pygame.draw.rect(self.image, BLACK, [8, 8, 4, 4])    # Eye
        pygame.draw.rect(self.image, BLACK, [18, 8, 4, 4])   # Eye
        pygame.draw.rect(self.image, BLACK, [8, 18, 14, 2])  # Angry mouth

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 1
        self.distance = 0

    def update(self):
        self.rect.x += 2 * self.direction
        self.distance += 2
        if self.distance >= 100:
            self.direction *= -1
            self.distance = 0

class Goal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill(BLACK)

        # Create a star pattern
        points = [
            (15, 0), (20, 10), (30, 12),
            (22, 20), (25, 30), (15, 25),
            (5, 30), (8, 20), (0, 12),
            (10, 10)
        ]
        pygame.draw.polygon(self.image, WHITE, points)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def draw_background(screen):
    screen.fill(BLACK)
    # Update star positions based on time
    global star_time
    star_time += 0.1  # Very slow movement - adjust this value to change speed

    # Near stars (move slightly faster)
    for x in range(-20 + (int(star_time) % 20), WINDOW_WIDTH + 20, 20):
        for y in range(0, WINDOW_HEIGHT, 20):
            pygame.draw.rect(screen, GRAY_DARK, [x, y, 2, 2])

    # Far stars (move slower)
    for x in range(-40 + (int(star_time/2) % 40), WINDOW_WIDTH + 40, 40):
        for y in range(0, WINDOW_HEIGHT, 40):
            pygame.draw.rect(screen, GRAY_LIGHT, [x, y, 1, 1])

# Set up the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pixel Platform Game")
clock = pygame.time.Clock()

# Create sprite groups
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
enemies = pygame.sprite.Group()
goals = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Create platforms
platform_list = [
    # Starting platform
    Platform(50, 500, 200, 20),

    # Middle platforms creating a path
    Platform(300, 400, 200, 20),
    Platform(100, 300, 200, 20),
    Platform(400, 250, 200, 20),

    # Higher platforms
    Platform(200, 150, 150, 20),
    Platform(500, 150, 150, 20),
]
for platform in platform_list:
    all_sprites.add(platform)
    platforms.add(platform)

# Create enemies
enemy_list = [
    Enemy(350, 370),  # On first middle platform
    Enemy(150, 270),  # On second middle platform
    Enemy(450, 220),  # On third middle platform
    Enemy(250, 120),  # On first top platform
]
for enemy in enemy_list:
    all_sprites.add(enemy)
    enemies.add(enemy)

# Create goal
goal = Goal(550, 100)
all_sprites.add(goal)
goals.add(goal)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player.can_jump:
                    player.velocity_y = JUMP_FORCE
                    player.can_jump = False
                elif player.double_jump:
                    player.velocity_y = JUMP_FORCE
                    player.double_jump = False

    # Handle continuous keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player.rect.x += PLAYER_SPEED

    # Update
    all_sprites.update()

    # Platform collisions
    hits = pygame.sprite.spritecollide(player, platforms, False)
    if hits:
        if player.velocity_y > 0:  # Falling down
            player.rect.bottom = hits[0].rect.top
            player.velocity_y = 0
            player.can_jump = True
            player.double_jump = True
        elif player.velocity_y < 0:  # Moving up (jumping)
            player.rect.top = hits[0].rect.bottom
            player.velocity_y = 0

    # Enemy collisions
    enemy_hits = pygame.sprite.spritecollide(player, enemies, False)
    if enemy_hits:
        # Check if player is falling and above the enemy (jumping on top)
        if player.velocity_y > 0 and player.rect.bottom < enemy_hits[0].rect.top + 10:
            # Kill the enemy
            enemy_hits[0].kill()
            # Bounce the player
            player.velocity_y = JUMP_FORCE / 2
        else:
            # Player dies
            if show_game_over():
                # Reset game state
                player.rect.x = 50
                player.rect.y = WINDOW_HEIGHT - 100
                player.velocity_y = 0
                player.can_jump = True
                player.double_jump = True
            else:
                running = False

    # Goal collision
    if pygame.sprite.spritecollide(player, goals, False):
        if show_winner():
            # Reset game state
            player.rect.x = 50
            player.rect.y = WINDOW_HEIGHT - 100
            player.velocity_y = 0
            player.can_jump = True
            player.double_jump = True
        else:
            running = False

    # Draw
    draw_background(screen)
    all_sprites.draw(screen)
    pygame.display.flip()
    all_sprites.draw(screen)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

pygame.quit()
