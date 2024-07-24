import pygame
import sys

from oregon_trail_game import WIDTH, HEIGHT

class Oregon:
    # setup to initialize the screen
    def __init__(self) -> None:
        print("Let's start")
        pygame.init()
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
    

    def start(self):
        """
        This is the main loop
        """
        exit = False
        # pygame.QUIT event means the user clicked X to close your window
        while not exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = True
            self.display.fill((99,99,99))
            pygame.display.flip