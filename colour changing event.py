import pygame as game
import random

game.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = game.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game.display.set_caption("Custom Event for Sprite Color Change")

WHITE = (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

sprite_size = 50
sprite1_x = SCREEN_WIDTH // 3
sprite1_y = SCREEN_HEIGHT // 2
sprite2_x = 2 * SCREEN_WIDTH // 3
sprite2_y = SCREEN_HEIGHT // 2

sprite1_color = random.choice(COLORS)
sprite2_color = random.choice(COLORS)

CHANGE_COLOR_EVENT = game.USEREVENT + 1
game.time.set_timer(CHANGE_COLOR_EVENT, 2000)

running = True
clock = game.time.Clock()

while running:
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False
        elif event.type == CHANGE_COLOR_EVENT:
            sprite1_color = random.choice(COLORS)
            sprite2_color = random.choice(COLORS)

    screen.fill(WHITE)

    game.draw.rect(screen, sprite1_color, (sprite1_x, sprite1_y, sprite_size, sprite_size))
    game.draw.rect(screen, sprite2_color, (sprite2_x, sprite2_y, sprite_size, sprite_size))

    game.display.flip()
    clock.tick(60)

game.quit()
