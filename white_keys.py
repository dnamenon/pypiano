

class White_Key:

    def __init__(self,piano):
        self.screen = piano.screen
        self.sets = piano.settings

        self.color = self.sets.white_key_color


        self.x = 0
        self.y = 0
        self.x1= 0
        self.y1 =0


        self.note_value = ''

    def draw_key(self,x):
        self.x = self.sets.leftrightend+x
        self.x1 = self.sets.white_key_width+self.x

        self.y = self.sets.topend
        self.y1 = self.y + self.sets.white_key_height



        self.screen.create_rectangle(self.x,self.y,self.x1,self.y1,fill=self.color)

    def assign_note_value(self, x):
        self.note_value = x