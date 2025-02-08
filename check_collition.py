#My left,right,forward,backward keys are not working
import pygame as game
import random

game.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = game.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game.display.set_caption("Sprite Collision Game")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

player_size = 50
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 5

enemy_size = 50
enemies = []
for _ in range(45):
    enemy_x = random.randint(0, SCREEN_WIDTH - enemy_size)
    enemy_y = random.randint(0, SCREEN_HEIGHT - enemy_size)
    enemies.append((enemy_x, enemy_y))

score = 0
font = game.font.Font(None, 36)  

running = True
clock = game.time.Clock()

while running:
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False

    keys = game.key.get_pressed()
    if keys[game.K_a]:
        player_x -= player_speed
    if keys[game.K_d]:
        player_x += player_speed
    if keys[game.K_w]:
        player_y -= player_speed
    if keys[game.K_s]:
        player_y += player_speed

    player_rect = game.Rect(player_x, player_y, player_size, player_size)
    for i, (enemy_x, enemy_y) in enumerate(enemies):
        enemy_rect = game.Rect(enemy_x, enemy_y, enemy_size, enemy_size)
        if player_rect.colliderect(enemy_rect):
            score += 1
            print(f"Score: {score}")
            enemies[i] = (random.randint(0, SCREEN_WIDTH - enemy_size), random.randint(0, SCREEN_HEIGHT - enemy_size))

    screen.fill(WHITE)
    game.draw.rect(screen, RED, player_rect)
    for enemy_x, enemy_y in enemies:
        game.draw.rect(screen, BLUE, game.Rect(enemy_x, enemy_y, enemy_size, enemy_size))

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    game.display.flip()
    clock.tick(60)

game.quit()
