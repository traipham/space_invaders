import pygame 
import random

import api.player as player
import time


WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720

WINDOW_BG_COLOR = (250, 234, 203)

class Bullet():
    """Bullet object that contains activity of bullet movement and bullet state"""
    def __init__(self, window, player):
        self._window = window
        self._player = player
        self._path = 'game_icon\\laser_bullet.png'
        self.img = pygame.image.load(self._path)
        self.xpos = self._player.xpos
        self.ypos = 0
        self.xpos_change = 0
        self.ypos_change = 0
        self.bullet_state = "ready"

        # TODO: fire multiple bullets by creating a queue and putting bullets in queue
    def fire_bullet(self):
        """
        Allow bullet to be fired and sets the bullet initial position (x,y), and display bullet
        """
        if self.bullet_state == "ready":
            self.bullet_state = "fire"
            self.xpos = self._player.xpos
            self.ypos = self._player.ypos + self._player.player_img.get_height()//2 # bullet will appear at half of spaceship
            self._window.blit(self.img, (self.xpos, self.ypos))
        else:
            print("Bullet is being fired!")
    
    def move_bullet(self, value: float):
        """
        Moves bullet when its being fired. Reset bullet position if bullet is in a ready state

        :param value(int): the distance that bullet should move every iteration of the game running
        """
        if self.bullet_state == "fire":
            self.ypos_change = value
            self.ypos += self.ypos_change
            if self.ypos == 0:
                self.bullet_state = "ready"
            self._window.blit(self.img, (self.xpos, self.ypos))
            return
        # TODO: Remove? may not be necessary
        if self.bullet_state == "ready":
            self.xpos = self._player.xpos
            self.ypos = self._player.ypos + self._player.player_img.get_height()//2 # bullet will appear at half of spaceship
    
    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, value):
        self._player = value