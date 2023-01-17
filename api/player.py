import pygame 
import random
import math
from queue import Queue
from pygame import mixer

import api.bullet as bullet 


WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720

WINDOW_BG_COLOR = (250, 234, 203)
# TODO: Add underscore to variable name to show "protected"(shouldn't be changed directly)
class Player(pygame.Surface):
    """
    Player object that controls player's movement, bullet activty and how bullet and player are displayed.
    """
    def __init__(self, window:pygame.Surface, img_path: str):
        self.window = window
        self.player_img = pygame.image.load(img_path)
        self.xpos = WINDOW_WIDTH//2 - (self.player_img.get_width()//2)
        self.ypos = WINDOW_HEIGHT - (self.player_img.get_height()*2)
        self.start_pos = (self.xpos, self.ypos)
        self.xpos_change = 0
        self.ypos_change = 0 
        self.score = 0

        # Bullet 
        ## bullet_state = "ready" = bullet is ready to be fired
        ## bullet_state = "fire" = bullet is currently moving
        self.bullets_queue:list[bullet.Bullet] = []
        self.open_fire = False
        pass
    
    def display(self):
        """
        Display player and bullet in window (if fired). Moves player and bullets in bullet list.
        
        """
        # move bulley in UI
        for b in self.bullets_queue:
            if b.ypos == 0:
                self.bullets_queue.remove(b)
                continue
            b.move_bullet(-0.5)
        self.move_player()
        self.window.blit(self.player_img, (self.xpos, self.ypos))           # to draw at coordinate
    
    def move_player(self):
        """Move player when key is pressed"""
        self.xpos += self.xpos_change
        self.ypos += self.ypos_change
        if self.xpos <= 0:
            self.xpos = 0
        elif self.xpos >= WINDOW_WIDTH-self.player_img.get_width():
            self.xpos = WINDOW_WIDTH-self.player_img.get_width()
    
    def fire_bullet(self):
        """
        Allow player to fire multiple bullets. There is a threshold of (6) bullets max
        """
        if len(self.bullets_queue) < 6 and self.open_fire:
            # plays sound when bullet is fired
            bullet_sound = mixer.Sound('sound\laser.wav')
            bullet_sound.play()
            # create bullet and fire it
            fired_bullet = bullet.Bullet(self.window, self)
            fired_bullet.fire_bullet()
            self.bullets_queue.append(fired_bullet)
            self.open_fire = False
        else:
            pass

    @property
    def open_fire(self):
        return self._open_fire

    @open_fire.setter
    def open_fire(self, value):
        self._open_fire = value
    
    @property
    def xpos(self):
        return self._xpos
    
    @xpos.setter
    def xpos(self, value:int):
        self._xpos = value
    
    @property 
    def ypos(self):
        return self._ypos

    @ypos.setter
    def ypos(self, value:int):
        self._ypos = value

    @property
    def xpos_change(self):
        return self._xpos_change
    
    @xpos_change.setter
    def xpos_change(self, value:float):
        self._xpos_change = value

    @property
    def ypos_change(self):
        return self._ypos_change

    @ypos_change.setter
    def ypos_change(self, value:float):
        self._ypos_change = value
    
    @property
    def window(self):
        return self._window

    @window.setter
    def window(self, win_value):
        self._window = win_value
