import pygame
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Game Screen with Rectangle and Text')
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
font = pygame.font.Font(None, 74)
text = font.render('Hello, Pygame!', True, black)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(white)
    pygame.draw.rect(screen, red, (100, 100, 200, 100))
    screen.blit(text, (250, 250))
    pygame.display.flip()
pygame.quit()
