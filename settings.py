import pygame


class Settings:


    # a class to store all settings
    def __init__(self):
        self.screen_width = 1201
        self.screen_height = 600
        self.topend = 150
        self.leftrightend = 93
        self.bg_color = (135, 206, 235)


        self.white_key_color = pygame.Color(255,255,255)
        self.white_key_width = 35
        self.white_key_height = 450

        self.key_border_color = pygame.Color(0,0,0)


        self.black_key_color = pygame.Color(0,0,0)

        self.black_key_height = 250
        self.black_key_width = 20

