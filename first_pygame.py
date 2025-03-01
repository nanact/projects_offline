import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('My First Game Screen')

white = (255, 255, 255)
black = (0, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    pygame.draw.rect(screen, black, (100, 100, 200, 100))

    pygame.display.flip()

pygame.quit()
