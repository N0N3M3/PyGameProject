from game import Game
import pygame


class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 70, 70)
        self.offset2 = 5
        self.offset = 175

    def draw_cursor(self):
        self.game.draw_text('*', 60, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.start_x, self.start_y = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 1.7
        self.settings_x, self.settings_y = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 1.5
        self.helping_x, self.helping_y = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 1.35
        self.state = "Начало"
        self.cursor_rect.midtop = (self.start_x - self.offset, self.start_y + self.offset2)

    def draw_cursor(self):
        self.game.draw_text('*', 60, self.cursor_rect.x, self.cursor_rect.y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.WHITE)
            self.game.draw_text('Волк ловит яйца', 60, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2.4)
            self.game.draw_text("Начать игру", 60, self.start_x, self.start_y)
            self.game.draw_text("Настройки", 60, self.settings_x, self.settings_y)
            self.game.draw_text("Помощь", 60, self.helping_x, self.helping_y)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Начало":
                self.cursor_rect.midtop = (self.settings_x - self.offset, self.settings_y + self.offset2)
                self.state = "Настройки"
            elif self.state == "Настройки":
                self.cursor_rect.midtop = (self.helping_x - self.offset, self.helping_y + self.offset2)
                self.state = "Помощь"
            elif self.state == "Помощь":
                self.cursor_rect.midtop = (self.start_x - self.offset, self.start_y + self.offset2)
                self.state = "Начало"
        elif self.game.UP_KEY:
            if self.state == "Начало":
                self.cursor_rect.midtop = (self.helping_x - self.offset, self.helping_y + self.offset2)
                self.state = "Помощь"
            elif self.state == "Помощь":
                self.cursor_rect.midtop = (self.settings_x - self.offset, self.settings_y + self.offset2)
                self.state = "Настройки"
            elif self.state == "Настройки":
                self.cursor_rect.midtop = (self.start_x - self.offset, self.start_y + self.offset2)
                self.state = "Начало"

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Начало':
                size = width, height = 1400, 900
                v = 250
                fps = 60
                eggs_speed = 3000
                clock = pygame.time.Clock()
                screen = pygame.display.set_mode(size)
                game = Game(screen, v, fps, eggs_speed, clock, width, height)
                game.run()
                pygame.quit()


