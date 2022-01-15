import pygame
from classes.wolf import Wolf
from classes.egg import Egg

pygame.init()
pygame.display.set_caption('Game')
size = width, height = 1400, 900
screen = pygame.display.set_mode(size)

running = True
v = 250  # пикселей в секунду
fps = 60
clock = pygame.time.Clock()
screen.fill((255, 255, 255))
wolf = Wolf(screen, width, height, 320)
egg = Egg(screen, width, height, v, fps)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                screen = wolf.set_position(4, screen)
            elif event.key == pygame.K_RIGHT:
                screen = wolf.set_position(2, screen)
            elif event.key == pygame.K_UP:
                screen = wolf.set_position(1, screen)
            elif event.key == pygame.K_DOWN:
                screen = wolf.set_position(3, screen)
    screen.fill((255, 255, 255))
    screen = egg.move(screen)
    screen = wolf.get_now_position(screen)
    clock.tick(fps)
    pygame.display.flip()
pygame.quit()
