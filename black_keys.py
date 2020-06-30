import pygame


class Black_Key:

    def __init__(self,piano):
        self.screen = piano.screen
        self.sets = piano.settings

        self.color = self.sets.black_key_color

        self.rect = pygame.Rect(0,150, self.sets.whitekey_width,self.sets.whitekey_height)
        self.border = pygame.Rect(0,150,self.sets.whitekey_width,self.sets.whitekey_height)
        self.border_color = self.sets.key_border_color

    def draw_key(self,x):
        self.rect.x = 93+x
        self.border.x = 93+x

        pygame.draw.rect(self.screen,self.color,self.rect)
        pygame.draw.rect(self.screen,self.border_color,self.border,width=1)