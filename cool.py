import pygame as game
import random

game.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = game.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game.display.set_caption("Two Sprites with Controls")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

sprite_size = 50
sprite1_x = SCREEN_WIDTH // 3
sprite1_y = SCREEN_HEIGHT // 2
sprite2_x = 2 * SCREEN_WIDTH // 3
sprite2_y = SCREEN_HEIGHT // 2

sprite_speed = 5

running = True
clock = game.time.Clock()

while running:
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False

    keys = game.key.get_pressed()
    if keys[game.K_LEFT]:
        sprite1_x -= sprite_speed
    if keys[game.K_RIGHT]:
        sprite1_x += sprite_speed
    if keys[game.K_UP]:
        sprite1_y -= sprite_speed
    if keys[game.K_DOWN]:
        sprite1_y += sprite_speed

    screen.fill(WHITE)

    game.draw.rect(screen, RED, (sprite1_x, sprite1_y, sprite_size, sprite_size))
    game.draw.rect(screen, BLUE, (sprite2_x, sprite2_y, sprite_size, sprite_size))

    game.display.flip()
    clock.tick(60)

game.quit()
