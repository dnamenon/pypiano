import pygame


class Black_Key:

    def __init__(self,piano):
        self.screen = piano.screen
        self.sets = piano.settings

        self.color = self.sets.black_key_color

        self.rect = pygame.Rect(0,0, self.sets.black_key_width,self.sets.black_key_height)
        self.border = pygame.Rect(0,0,self.sets.black_key_width,self.sets.black_key_height)
        self.border_color = self.sets.key_border_color

    def draw_key_1(self,x,c1, c2):
        octave = 35*7
        a = c2 % 2
        if a == 0:
             a = 2
        self.rect.x = 93 + (2*a*x) + (octave*c1)
        self.border.x = self.rect.x
        self.rect.y = 150
        self.border.y = self.rect.y
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.border_color, self.border, width=1)



    def draw_key_2(self, x, c1, c2):
        octave = 35 * 7
        a = c2 % 3
        if a == 0:
             a = 3
        self.rect.x = 233 + (2 * a * x) + (octave * c1)
        self.border.x = self.rect.x
        self.rect.y =150
        self.border.y = self.rect. y

        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.border_color, self.border, width=1)
