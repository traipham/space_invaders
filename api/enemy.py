import pathlib
import pygame 
import os
import random

import math
from pygame import mixer

WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720

WINDOW_BG_COLOR = (250, 234, 203)

class Enemy(pygame.Surface):
    def __init__(self, window:pygame.Surface, img_path: str):
        self.num_row = 10
        self.window = window
        file_dir = os.path.dirname(__file__)
        image_path = pathlib.Path(file_dir).parent.absolute()
        self.enemey_1_img = pygame.image.load(f"{image_path}/{img_path}")
        self.xpos = WINDOW_WIDTH//2 - (self.enemey_1_img.get_width()//2)
        self.ypos = (self.enemey_1_img.get_height()*2)
        self.xpos_change = -0.8
        self.ypos_change = (WINDOW_HEIGHT//2 - self.enemey_1_img.get_height())//self.num_row 
        self.xpos_accel = 0
        self.start_pos = (self.xpos, self.ypos)
        pass
    
    def display_enemey_1(self):
        """Display enemey_1 to window"""
        self.move_enemey_1()
        self.window.blit(self.enemey_1_img, (self.xpos, self.ypos))           # to draw at coordinate
    
    def move_enemey_1(self):
        self.xpos += self.xpos_change
        if self.xpos <= 0:
            self.xpos_change = 1 + self.xpos_accel
            self.ypos += self.ypos_change
            self.incr_accel()
        elif self.xpos >= WINDOW_WIDTH-self.enemey_1_img.get_width():
            self.xpos_change = -1 - self.xpos_accel
            self.ypos += self.ypos_change
            self.incr_accel()
    
    def incr_accel(self):
        self.xpos_accel += 0.2

    def respawn(self): 
        self.xpos = random.randint(0, WINDOW_WIDTH-(self.enemey_1_img.get_width()))
        self.ypos = random.randint(0, (WINDOW_HEIGHT//2)-self.enemey_1_img.get_height())
        self.xpos_accel = 0
        pass

    def isCollision(self, bullet_xpos, bullet_ypos):
        distance = math.sqrt(math.pow(self.xpos-bullet_xpos, 2) + math.pow(self.ypos-bullet_ypos, 2))
        if distance < self.enemey_1_img.get_height():
            # play explosion sound
            explosion_sound = mixer.Sound('./sound/explosion.wav')
            explosion_sound.set_volume(0.5)
            explosion_sound.play()
            return True
        else:
            return False

    def isGameOver(self, window_height:int):
        if self.ypos >= window_height-50:
            return True
        else:
            return False

    def despawn(self):
        if self.isCollision():
            pass
        pass