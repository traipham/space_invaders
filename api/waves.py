import pygame
import random

import math
from api.enemy import Enemy
from api.bullet import Bullet

WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720

WINDOW_BG_COLOR = (250, 234, 203)

MAX_ROW = 5
MAX_COL = 5
class Waves:
    """Waves object is a list of enemies. This class controls enemy movement, collision, and game over"""
    def __init__(self, window:pygame.surface, img_path:str, num_row:int=1 , num_col:int = 1):
        self.enemies: list[list[Enemy]] = [[] for _ in range(num_row)]
        self.num_collision:int =0
        self.game_over = False
        self.img_path = img_path
        # Add enemies to list, initiate row 
        for col in range(num_col):
            # Initialize 2D list of enemies
            for row in range(num_row):
                new_enemy = Enemy(window, self.img_path)
                new_enemy.xpos += new_enemy.enemey_1_img.get_width()*row
                if col != 0: 
                    new_enemy.ypos += new_enemy.enemey_1_img.get_height()*col
                self.enemies[col].append(new_enemy)

    def display_wave(self):
        """Display wave of enemies"""
        for row in self.enemies:
            for enemy in row:
                enemy.display_enemey_1()

    def is_collision(self, bullets_list:list[Bullet]):
        """Check for collision for each Enemy in list"""
        if len(bullets_list) == 0:
            return 0
        self.num_collision = 0
        for b in bullets_list:
            for row in self.enemies:
                for e in row:
                    collision = e.isCollision(b.xpos, b.ypos)
                    if collision:
                        row.remove(e)
                        try:
                            # when a bullet hits multiple target, bullet should only be removed once
                            bullets_list.remove(b)
                        except:
                            pass
                        self.num_collision += 1
        return self.num_collision

    # TODO: remove all enemies
    def remove_all(self):
        self.enemies.clear()

    # TODO: game_over should be in a game class
    def is_game_over(self):
        for row in self.enemies:
            for e in row:
                if e.isGameOver():
                    self.enemies.clear()
                    self.game_over = True
                    return self.game_over
        return self.game_over

