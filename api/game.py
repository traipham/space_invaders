import pygame 
import random
from api.player import Player
from api.enemy import Enemy
from api.waves import Waves
from pygame import mixer
from api.button import Button

WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720

WINDOW_BG_COLOR = (250, 234, 203)

class Game:
    def __init__(self, window:pygame.Surface):
        # elements in game
        self.player_img_path = 'game_icon\\player.png'
        self.enemy_img_path = "C:\\Users\\traip\\OneDrive\\Desktop\\Python_Learning\\Projects\\learning_pygame\\game_icon\\enemy_1.png"
        self.window = window
        self.player = Player(window, self.player_img_path)
        self.waves = Waves(window, self.enemy_img_path, 3, 3)
        # Logistic elemets
        self.score = 0
        self.game_over = False
        self.running = True
        self.display_menu = True
        # display main menu

        # play music
        background_sound = mixer.Sound('sound\\background.wav')
        background_sound.set_volume(0.5)
        background_sound.play()

    def main_menu(self):
        pygame.display.set_caption("Menu")
        while self.display_menu:
            self.window.blit(WINDOW_BG_COLOR, (0,0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT_FONT = pygame.font.Font('freesansbold.ttf', 100)
            MENU_TEXT = MENU_TEXT_FONT.render("Main Menu", True, (255,255,255))
            MENU_RECT = MENU_TEXT.get_rect(center=(640,100))

            PLAY_BUTTON = Button(self.window)


    def run(self):
        while self.running:
            # Change window color
            self.window.fill(WINDOW_BG_COLOR)

            # Go through event of pygame, and make screen run continiously
            for event in pygame.event.get():
                if event.type == pygame.QUIT:       # When click the close window button
                    self.running = False
                # when there's a keyboard input, check if it's left or right movement
                if event.type == pygame.KEYDOWN:
                    if (event.key in (pygame.K_a, pygame.K_LEFT)):
                        self.player.xpos_change = -1.5
                        pygame.key.set_repeat(1, 1)
                    if (event.key in (pygame.K_d, pygame.K_RIGHT)):
                        self.player.xpos_change = 1.5
                        pygame.key.set_repeat(1, 1)
                    if (event.key == pygame.K_SPACE):
                        self.player.fire_bullet()  # initiate bullet object
                if event.type == pygame.KEYUP:
                    if event.key in (pygame.K_a, pygame.K_LEFT, pygame.K_d, pygame.K_RIGHT):
                        self.player.xpos_change = 0
                    if event.key == pygame.K_SPACE:
                        self.player.open_fire = True

            if self.is_game_over():
                self.show_game_over(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

            # TODO: Put into Player function
            self.score += self.waves.is_collision(self.player.bullets_queue)
            self.show_score(10, 10)

            # draw self.player, enemy, and bullet
            self.waves.display_wave()
            self.player.display()
            pygame.display.update()
    
    def show_score(self, x, y):
        font = pygame.font.Font('freesansbold.ttf', 32)
        score = font.render(f"Score: {self.score}", True, (255, 100, 100))
        self.window.blit(score, (x, y))
    
    def show_game_over(self, x, y):
        game_over_font = pygame.font.Font('freesansbold.ttf', 64)
        """Display game_over"""
        game_over_rend = game_over_font.render("GAME OVER!", True, (255, 100, 100))
        self.window.blit(game_over_rend, (x, y))

    def is_game_over(self) -> bool:
        if len(self.waves.enemies) != 0:
            for row in self.waves.enemies:
                for e in row:
                    if e.isGameOver():
                        self.game_over = True
                        self.waves.remove_all()
                        return self.game_over
        return self.game_over

# if __name__ == "__main__":

#     # initilize pygame window 
#     pygame.init()
#     window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

#     # Title and Icon
#     pygame.display.set_caption("Space Invaders")
#     icon = pygame.image.load('game_icon\\window_icon.png')
#     pygame.display.set_icon(icon)

#     # Set players and Enemy
#     player = Player(window, 'game_icon\\player.png')
#     enemy = Enemy(window, 'game_icon\\enemy_1.png')
#     waves = Waves(
#         window, "C:\\Users\\traip\\OneDrive\\Desktop\\Python_Learning\\Projects\\learning_pygame\\game_icon\\enemy_1.png", 3, 3)
#     score = 0

#     font = pygame.font.Font('freesansbold.ttf', 32)
#     textX = 10
#     textY = 10

#     # game over text
#     game_over_font = pygame.font.Font('freesansbold.ttf', 64)
#     game_over = False
#     # Running game, event callbacks, and interactions
#     running = True
#     while running:

#         # Change window color 
#         window.fill(WINDOW_BG_COLOR)

#         # Go through event of pygame, and make screen run continiously
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:       # When click the close window button
#                 running = False
#             # when there's a keyboard input, check if it's left or right movement
#             if event.type == pygame.KEYDOWN:
#                 if (event.key in (pygame.K_a, pygame.K_LEFT)):
#                     player.xpos_change = -0.3
#                     pygame.key.set_repeat(1, 1)
#                 if (event.key in (pygame.K_d, pygame.K_RIGHT)):
#                     player.xpos_change = 0.3
#                     pygame.key.set_repeat(1, 1)
#                 if (event.key == pygame.K_SPACE):
#                     player.fire_bullet() # initiate bullet object
#             if event.type == pygame.KEYUP:
#                 if event.key in (pygame.K_a, pygame.K_LEFT, pygame.K_d, pygame.K_RIGHT):
#                     player.xpos_change = 0
#                 if event.key == pygame.K_SPACE:
#                     player.open_fire = True

#         if is_game_over(waves):
#             show_game_over(game_over_font, WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

#         # TODO: Put into Player function 
#         score += waves.is_collision(player.bullets_queue)   
#         show_score(font, score, textX, textY)

#         # draw player, enemy, and bullet
#         waves.display_wave()
#         player.display()
#         pygame.display.update()                 # Constantly call update when UI changes 

