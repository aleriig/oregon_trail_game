
import pygame
from oregon_trail_game.__init__ import *

# Define button class
class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        
    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect, 2)
        font = pygame.font.Font('resources/fonts/GamePlayed-vYL7.ttf', 24)
        text = font.render(self.text, True, WHITE)
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)
        
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Create buttons
main_buttons = [
    Button(30, 100, 150, 30, "GAME HISTORY"),
    Button(30, 140, 150, 30, "TUTORIAL"),
    Button(30, 180, 150, 30, "SETTINGS"),
    Button(WIDTH - 240, 100, 220, 30, "TRAVEL THE TRAIL"),
    Button(WIDTH - 240, 140, 220, 30, "LEARN ABOUT THE TRAIL"),
    Button(WIDTH - 240, 220, 220, 30, "CREDITS")
]

# class Scene:
#     def __init__(self, screen):
#         self.screen = screen
        
#     def main_loop(self):
#         pass

# class FrontPage(Scene):
#     def main_lopp(self):
#         exit = False
#         while not exit:
#             for event in pg.event.get():  
#                 if event.type == pg.QUIT:
#                     exit = True
#             self.screen.fill((99, 99 , 99))     