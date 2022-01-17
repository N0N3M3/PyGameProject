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
        self.helping_x, self.helping_y = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 1.5
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
            self.game.draw_text("Помощь", 60, self.helping_x, self.helping_y)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Начало":
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
                self.cursor_rect.midtop = (self.start_x - self.offset, self.start_y + self.offset2)
                self.state = "Начало"

    def check_input(self, game=None):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == "Помощь":
                self.game.curr_menu = self.game.helping
            elif self.state == 'Начало':
                game = StartGame(game)
                game.start()
            self.run_display = False


class StartGame:
    def __init__(self, game):
        self.game = game
        self.width = 1400
        self.height = 900
        self.size = self.width, self.height
        self.v = 250
        self.fps = 60
        self.eggs_speed = 3000
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.size)

    def start(self):
        game = Game(self.screen, self.v, self.fps, self.eggs_speed,
                    self.clock, self.width, self.height)
        game.run()
        
    def draw_text(self, text, size, x, y):
        font = pygame.font.Font("data/Dited.otf", size)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def game_over(self):
        self.screen.fill((255, 255, 255))
        self.draw_text('Игра окончена!', 80, self.height / 2, self.width / 2.4)
        self.draw_text(f"Ваш результат: {self.game.eggs_counter - 3}", 60, self.height / 2, self.width / 2)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            game = Game(self.screen, self.v, self.fps, self.eggs_speed, self.clock, 
                        self.width, self.height)
            game.run()
        elif keys[pygame.K_BACKSPACE]:
            pygame.quit()
            quit()


class HelpMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.WHITE)
            self.game.draw_text('Помощь!', 80, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2.4)
            self.game.draw_text('При помощи стрелочек управляй волком,', 60, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2)
            self.game.draw_text('чтобы словить как можно больше яиц.', 60, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 1.8)
            self.game.draw_text('Чтобы вернуться обратно нажми bakspace.', 60, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 1.4)
            self.blit_screen()
