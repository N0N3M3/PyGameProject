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
eggs_speed = 3000  # 3000
counter_of_not_caught_eggs = 0
time_delta_limit = 500
EGGS_CREATE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(EGGS_CREATE_EVENT, eggs_speed)
clock = pygame.time.Clock()
screen.fill((255, 255, 255))
eggs_counter = 0
wolf = Wolf(screen, width, height, 320)
eggs_pool = [Egg(screen, width, height, v, fps)]
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
        elif event.type == EGGS_CREATE_EVENT:
            eggs_pool.append(Egg(screen, width, height, v, fps))
            if eggs_speed > time_delta_limit:
                eggs_counter += 1
                if eggs_counter % 10 == 0:
                    eggs_speed -= 300
                    pygame.time.set_timer(EGGS_CREATE_EVENT, 0)
                    pygame.time.set_timer(EGGS_CREATE_EVENT, eggs_speed)
                    print(eggs_speed)

    screen.fill((255, 255, 255))
    for egg in eggs_pool:
        screen = egg.move(screen)
        if not egg.check_position():
            eggs_pool.remove(egg)
            if egg.side != wolf.position:
                print(egg.side, wolf.position)
                counter_of_not_caught_eggs += 1
                if counter_of_not_caught_eggs == 3:
                    pygame.quit()

    screen = wolf.get_now_position(screen)
    clock.tick(fps)
    pygame.display.flip()
pygame.quit()
