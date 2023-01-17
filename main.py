import pygame
import random

from api.button import Button
import api.game as game 


WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720
WINDOW_BG_COLOR = (250, 234, 203)

WHITE = (255,255,255)

if __name__ == "__main__":
    # initilize pygame window
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # Title and Icon
    pygame.display.set_caption("Space Invaders")
    icon = pygame.image.load('game_icon\\window_icon.png')
    pygame.display.set_icon(icon)

    game = game.Game(window)
    start_button = Button(window)
    start_click = False
    run = True
    window.fill((255, 255, 255))
    while not start_click:
        start_button.check_clicked()
        if start_button.quit:
            run = False
            break
        start_click = start_button.is_clicked
        start_button.display_button()
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False
                break
        pygame.display.update()

    if run:
        game.run()