import sys

import pygame

from settings import Settings


class PyPiano:
    """overall class to manage game assets and behavior"""

    def __init__(self):

        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        pygame.display.set_caption("pyPiano")

    def main_loop(self):

        while True:

            self._event_handler()

            self._draw_screen()

    def _draw_screen(self):
        # redraw screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)

        pygame.display.flip()

    def _event_handler(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == '__main__':
    piano = PyPiano()
    piano.main_loop()