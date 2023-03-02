import asyncio
import pygame
import os
import random

from api.button import Button
from api.game import Game


WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720
WINDOW_BG_COLOR = (250, 234, 203)

WHITE = (255,255,255)

async def main():
    # initilize pygame window
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # Title and Icon
    pygame.display.set_caption("Space Invaders")
    full_path = os.path.dirname(__file__)
    icon = pygame.image.load(f'{full_path}/game_icon/window_icon.png')
    pygame.display.set_icon(icon)

    game = Game(window)
    start_button = Button(window=window, text="Start",
                          text_color=WHITE, index=1)
    end_button = Button(window=window, text="End",
                        text_color=(150, 255, 255), index=2)
    start_click = False
    run = True
    window.fill(WHITE)
    while not start_click:
        start_button.check_clicked()
        end_button.check_clicked()
        start_click = start_button.is_clicked
        start_button.display_button()
        end_button.display_button()
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT or end_button.is_clicked:
                run = False
                break
        pygame.display.update()
        await asyncio.sleep(0)
        if not run:
            break
    if run:
        await game.run()

if __name__ == "__main__":
    asyncio.run(main())