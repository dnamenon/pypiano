import pygame


class Whitekey:

    def __init__(self,piano):
        self.screen = piano.screen
        self.sets = piano.settings

        self.color = self.sets.whitekey_color

        self.rect = pygame.Rect(100,150, self.sets.whitekey_width,self.sets.whitekey_height)

    def draw_key(self):
        pygame.draw.rect(self.screen,self.color,self.rect)