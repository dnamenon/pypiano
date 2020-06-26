import sys

import pygame

from settings import Settings


class AlienInvasion:
    """overall class to manage game assets and behavior"""

    def __init__(self):
        """initialize game """
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.screen.fill(self.settings.bg_color)

        pygame.display.set_caption("pyPiano")