import pygame
from classes.wolf import Wolf
from classes.egg import Egg
from utils import load_image


class Game:
    def __init__(self, _screen: pygame.Surface, _v: int, _fps: int, _eggs_speed: int, _clock: pygame.time.Clock,
                 _width: int, _height: int):
        pygame.display.set_caption('Game')
        self.size = self.width, self.height = _width, _height
        self.screen = _screen
        self.running = True
        self.v = _v  # пикселей в секунду
        self.fps = _fps
        self.grass = pygame.transform.scale(load_image('../data/grass.png', colorkey=-1), (self.width, 20))
        self.background = pygame.transform.scale(load_image('../data/scene.png', colorkey=-1), (self.width, self.height))
        self.eggs_speed = _eggs_speed
        self.counter_of_not_caught_eggs = 0
        self.time_delta_limit = 500
        self.EGGS_CREATE_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.EGGS_CREATE_EVENT, _eggs_speed)
        self.clock = _clock
        self.eggs_counter = 0

    def run(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.grass, (0, self.height - 20))

        wolf = Wolf(self.screen, self.width, self.height, 480, 750)
        eggs_pool = [Egg(self.screen, self.width, self.height, self.v, self.fps)]
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.screen = wolf.set_position(4, self.screen)
                    elif event.key == pygame.K_RIGHT:
                        self.screen = wolf.set_position(2, self.screen)
                    elif event.key == pygame.K_UP:
                        self.screen = wolf.set_position(1, self.screen)
                    elif event.key == pygame.K_DOWN:
                        self.screen = wolf.set_position(3, self.screen)
                elif event.type == self.EGGS_CREATE_EVENT:
                    eggs_pool.append(Egg(self.screen, self.width, self.height, self.v, self.fps))
                    if self.eggs_speed > self.time_delta_limit:
                        self.eggs_counter += 1
                        if self.eggs_counter % 10 == 0:
                            self.eggs_speed -= 300
                            pygame.time.set_timer(self.EGGS_CREATE_EVENT, 0)
                            pygame.time.set_timer(self.EGGS_CREATE_EVENT, self.eggs_speed)
                            print(self.eggs_speed)
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.grass, (0, self.height - 20))

            for egg in eggs_pool:
                self.screen = egg.move(self.screen)
                if not egg.check_position():
                    eggs_pool.remove(egg)
                    if egg.side != wolf.position:
                        print(egg.side, wolf.position)
                        self.counter_of_not_caught_eggs += 1
                        if self.counter_of_not_caught_eggs == 3:
                            self.running = False
            self.screen = wolf.get_now_position(self.screen)
            self.clock.tick(self.fps)
            pygame.display.flip()
        return self.game_over()

    def game_over(self):
        self.screen.fill((255, 255, 255))
        self.draw_text('Игра окончена!', 80, self.height / 2, self.width / 2.4)
        self.draw_text(f"Ваш результат: {self.eggs_counter - 3}", 60, self.height / 2, self.width / 2)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            game.run()
        elif keys[pygame.K_BACKSPACE]:
            pygame.quit()
            quit()

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font("data/Dited.otf", size)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1400, 900
    v = 250
    fps = 60
    eggs_speed = 3000
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size)
    game = Game(screen, v, fps, eggs_speed, clock, width, height)
    game.run()
    pygame.quit()
