import pygame


class White_Key:

    def __init__(self,piano):
        self.screen = piano.screen
        self.sets = piano.settings

        self.color = self.sets.white_key_color

        self.rect = pygame.Rect(0,0, self.sets.white_key_width,self.sets.white_key_height)
        self.border = pygame.Rect(0,0,self.sets.white_key_width,self.sets.white_key_height)
        self.border_color = self.sets.key_border_color

    def draw_key(self,x):
        self.rect.x = self.sets.leftrightend+x
        self.border.x = self.sets.leftrightend+x
        self.rect.y = self.sets.topend
        self.border.y = self.sets.topend

        pygame.draw.rect(self.screen,self.color,self.rect)
        pygame.draw.rect(self.screen,self.border_color,self.border,width=1)