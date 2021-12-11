import pygame
import random


class Egg:
    def __init__(self, screen: pygame.Surface, width_screen, height_screen, speed):
        self.screen = screen
        self.width_screen = width_screen
        self.height_screen = height_screen
        self.speed = speed
        self.side = random.randint(1, 4)

    def _construct_egg(self):
        ...
