import sys

import pygame

from settings import Settings
from whitekeys import Whitekey


class PyPiano:
    """overall class to manage game assets and behavior"""

    def __init__(self):

        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )


        pygame.display.set_caption("pyPiano")


        self.whitekeys = []
        self._make_keys(self.whitekeys)
        self.screen.fill(self.settings.bg_color)
        self._draw_whitekeys()
        pygame.display.flip()


    def main_loop(self):

        while True:

            self._event_handler()





    def _event_handler(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _make_keys(self,listofkeys):
        for value in range(0,29):
            listofkeys.append(Whitekey(self))

    def _draw_whitekeys(self):
        count = 0

        for key in self.whitekeys:
            key.draw_key(count*34)
            count +=1


if __name__ == '__main__':
    piano = PyPiano()
    piano.main_loop()