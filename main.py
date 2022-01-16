from menu1 import Window

g = Window()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
