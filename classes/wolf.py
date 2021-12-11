import pygame
from utils import *


class Wolf:
    def __init__(self, screen: pygame.Surface, width_screen: int, height_screen: int, height_wolf: int):
        self.screen = screen
        self.width_screen = width_screen
        self.height_screen = height_screen
        self.height_wolf = height_wolf
        self.position = 4  # здесь направление стрелок: 1 - 4, счет с левого верхнего угла до нижнего левого по ЧС
        self._construct_wolf()

    def _construct_wolf(self):
        image = load_image('../data/wolf_down_left.png', colorkey=(255, 255, 255))
        self.screen.blit(image, (self.width_screen // 2 - self.height_wolf, self.height_screen - self.height_wolf))

    def set_position(self, position):
        """
        Установка новой позиции
        :param position: число 1-4, счет с верхней стрелочки до самой левой
        :return:
        """
        _dictionary_of_positions = {
            'up_left': 1,
            'up_right': 2,
            'down_right': 3,
            'down_left': 4
        }
        old_vertical_position = 'up' if self.position < 3 else 'down'

        old_horizontal_position = 'left' if self.position in [1, 4] else 'right'
        if position == 1:
            path = f"up_{old_horizontal_position}"
        elif position == 2:
            path = f"{old_vertical_position}_right"
        elif position == 3:
            path = f"down_{old_horizontal_position}"
        else:
            path = f"{old_vertical_position}_left"
        self.position = _dictionary_of_positions.get(path)
        self.screen.fill((0, 205, 0))
        image = load_image(f'../data/wolf_{path}.png', colorkey=(255, 255, 255))
        self.screen.blit(image, (self.width_screen // 2 - self.height_wolf, self.height_screen - self.height_wolf))


