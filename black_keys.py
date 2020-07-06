


class Black_Key:

    def __init__(self,piano):
        self.screen = piano.screen
        self.sets = piano.settings

        self.color = self.sets.black_key_color


        self.border_color = self.sets.key_border_color

        self.note_value = ''
        self.x = 0
        self.y = 0
        self.x1 = 0
        self.y1 = 0

    def draw_key_1(self,x,c1, c2):
        octave = 35*7
        a = c2 % 2
        if a == 0:
             a = 2
        self.x = 93 + (2*a*x) + (octave*c1) - x
        self.x1 = self.sets.black_key_width + x

        self.y =150
        self.y = self.sets.black_key_height + self.y



        self.rect = self.screen.create_rectangle(self.x,self.y,self.x1,self.y1, fill=self.sets.black_key_color)




    def draw_key_2(self, x, c1, c2):
        octave = 35 * 7
        a = c2 % 3
        if a == 0:
             a = 3
        self.x = 198 + (2 * a * x) + (octave * c1) - x
        self.x1 = self.sets.black_key_width + x

        self.y =150
        self.y = self.sets.black_key_height + self.y


        self.rect = self.screen.create_rectangle(self.x,self.y,self.x1,self.y1, fill=self.sets.black_key_color)


    def assign_note_value(self,x):
        self.note_value = x
