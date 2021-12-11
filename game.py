import pygame
from classes.wolf import Wolf
# from classes.egg import ..

pygame.init()
pygame.display.set_caption('Game')
size = width, height = 1400, 900
screen = pygame.display.set_mode(size)

running = True
x_pos = 0
v = 250  # пикселей в секунду
fps = 60
clock = pygame.time.Clock()
screen.fill((0, 205, 0))
wolf = Wolf(screen, width, height, 320)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                wolf.set_position(4)
            elif event.key == pygame.K_RIGHT:
                wolf.set_position(2)
            elif event.key == pygame.K_UP:
                wolf.set_position(1)
            elif event.key == pygame.K_DOWN:
                wolf.set_position(3)

    x_pos += v / fps
    clock.tick(fps)
    pygame.display.flip()
pygame.quit()
