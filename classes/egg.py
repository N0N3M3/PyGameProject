import pygame
import random


class Egg:
    def __init__(self, screen: pygame.Surface, width_screen, height_screen, speed: int, fps: int):
        self.screen = screen
        self.width_screen = width_screen
        self.height_screen = height_screen
        self.speed = speed
        self.fps = fps
        self.egg_size = 20
        self.side = random.randint(1, 4)
        self.coords = None
        self.delta_y = self.speed // self.fps - 1
        self._construct_egg()

    def _construct_egg(self):
        if self.side == 1:
            coords = (0 + self.egg_size, int(self.height_screen * .18))
        elif self.side == 2:
            coords = (self.width_screen - self.egg_size, int(self.height_screen * .18))
        elif self.side == 3:
            coords = (self.width_screen - self.egg_size, int(self.height_screen * .45))
        else:
            coords = (0 + self.egg_size, int(self.height_screen * .45))
        self.coords = coords

        pygame.draw.circle(self.screen, pygame.Color(0, 0, 0), coords, self.egg_size)

    def move(self, screen: pygame.Surface):
        delta_x = self.speed // self.fps
        delta_x = delta_x if self.side == 1 or self.side == 4 else -delta_x
        self.coords = (self.coords[0] + delta_x, self.coords[1] + self.delta_y)
        pygame.draw.circle(screen, pygame.Color(0, 0, 0), self.coords, self.egg_size)
        return screen

    def check_position(self):
        """
        проверяет не зашло ли яйцо за условную границу
        :return: bool значение
        """
        if self.side == 1 or self.side == 4:
            return self.coords[0] < self.width_screen // 3 and self.coords[1] < self.height_screen - self.egg_size
        else:
            return self.coords[0] > self.width_screen // 3 * 2 and self.coords[1] < self.height_screen - self.egg_size
