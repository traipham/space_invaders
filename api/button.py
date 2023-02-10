import pygame
import time

WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720

WINDOW_BG_COLOR = (250, 234, 203)
BUTTON_TEXT_SIZE_ORIG = 100

STEEL_BLUE = (70, 130, 180)
LIGHT_STEEL_BLUE = (150, 180, 230)
BLACK = (0, 0, 0)

FONT = 'freesansbold.ttf'
class Button():
    def __init__(self, window:pygame.Surface, text:str, text_color:tuple[int], index:int):
        """Temporary fix with indexing button display"""
        self.window = window
        self.text_size = int(BUTTON_TEXT_SIZE_ORIG*((self.window.get_height() + self.window.get_width())/(WINDOW_WIDTH + WINDOW_HEIGHT)))
        self.fade_color = (150, 150, 150)
        self.text_color = text_color
        self.text = text
        self.button_font = pygame.font.Font(FONT, self.text_size)
        # self.end_font = pygame.font.Font(FONT, self.text_size)
        self.button_text = self.button_font.render(self.text, True, self.text_color)
        # self.end_text = self.end_font.render("Quit", True, (200, 200,255))

        self.button_rect = self.button_text.get_rect(center=(self.window.get_width()//2,self.window.get_height()//4*index))
        self.button_rect_color = BLACK
        # self.end_rect = self.end_text.get_rect(center=(self.window.get_width()//2,self.window.get_height()//2))
        # self.end_rect_color = BLACK
        self.is_clicked = False

    def display_button(self):
        pygame.draw.rect(self.window, self.button_rect_color, self.button_rect)
        # pygame.draw.rect(self.window, self.end_rect_color, self.end_rect)
        self.window.blit(self.button_text, (self.button_rect.x ,self.button_rect.y))
        # self.window.blit(self.end_text, (self.end_rect.x ,self.end_rect.y))
    
    # def button_clicked(self):
        """Change color of button on click"""
    #     self.button_text = self.button_font.render("button", True, (200, 200, 200))
    #     self.button_rec_color = LIGHT_STEEL_BLUE
    #     pygame.draw.rect(self.window, self.button_rec_color, self.button_rec)
    #     self.window.blit(self.button_text, (self.button_rec.x, self.button_rec.y))

    def check_clicked(self):
        # get mouse position
        pos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(pos):
            # change color when mouse hovers
            self.button_text = self.button_font.render(self.text, True, self.fade_color)
            self.button_rect_color = STEEL_BLUE
            if pygame.mouse.get_pressed()[0] == 1 and self.is_clicked == False:
                self.is_clicked = True
        else: 
            self.button_text = self.button_font.render(self.text, True, self.text_color)
            self.start_rect_color = BLACK

    @property
    def clicked(self):
        return self.is_clicked
    
    @clicked.setter
    def clicked(self, val:bool):
        self.is_clicked = val

        # if self.end_rect.collidepoint(pos):
        #     self.end_text = self.end_font.render("Quit", True, (150, 150, 150))
        #     self.end_rect_color = STEEL_BLUE
        #     if pygame.mouse.get_pressed()[0] == 1 and self.is_clicked == False:
        #         self.quit = True
        # else: 
        #     self.end_text = self.end_font.render("Quit", True, (255,255,255))
        #     self.end_rect_color = BLACK


# if __name__ == "__main__":
#     # initilize pygame window
#     pygame.init()
#     window = pygame.display.set_mode((800, 600))

#     # Title and Icon
#     pygame.display.set_caption("Space Invaders")
#     icon = pygame.image.load('game_icon\\window_icon.png')
#     pygame.display.set_icon(icon)

#     button = Button(window)
#     run = True
#     start_click = False
#     while run:
#         window.fill(WINDOW_BG_COLOR)
#         if not start_click:
#             start_click = button.check_clicked()
#             if start_click:
#                 print("Hello")
#             button.display_button()
#         for event in pygame.event.get():
#             # quit game
#             if event.type == pygame.QUIT:
#                 run = False
#         pygame.display.update()
#     pygame.quit()

