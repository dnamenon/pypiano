import sys

import pygame
import mido
from mido import messages
import rtmidi

from settings import Settings
from white_keys import White_Key
from black_keys import Black_Key



class PyPiano:
    """overall class to manage game assets and behavior"""

    def __init__(self):

        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )


        pygame.display.set_caption("pyPiano")

        self.rt = rtmidi.MidiIn()

        if self.rt.get_port_count() != 0:
            self.midi_in = mido.open_input('Launchkey MK2 49 Launchkey MIDI')
        else:
            self.midi_in = mido.open_input('keyboard', virtual=True)


        self.keys = []
        self._make_keys(self.keys)

        self.key_midi = {}
        self._keystomidi(self.key_midi)

        self.screen.fill(self.settings.bg_color)
        self._draw_keys()
        pygame.display.flip()


    def main_loop(self):

        while True:

            self._midi_handler()

            self._event_handler()







    def _event_handler(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                del self.midi_in
                sys.exit()

    def _make_keys(self,listofkeys):

        for value in range(1,30):

            listofkeys.append(White_Key(self))


            if (value % 7 == 1 or value % 7 == 2 or value % 7 == 4 or value % 7 == 5 or value % 7 == 6) and value < 29:
                #the extra c on top shouldn't have a black key assigned to it
                listofkeys.append(Black_Key(self))


    def _draw_keys(self):
        count = 0
        count2 = 1
        count3 = 1


        for key in self.keys:
            if type(key) is White_Key:
                key.draw_key((count)*35)
                pygame.display.flip()
                count +=1
        count = 0

        for key in self.keys:

            if count%7 <=3 and type(key) is Black_Key:

                self._draw_black_keys_1(count,count2,key)

                count2 +=1
            elif count%7 > 3 and type(key) is Black_Key:

                self._draw_black_keys_2(count,count3,key)

                count3 += 1
            else:
                count += 1





    def _draw_black_keys_1(self,num1,num2,key):
        count1 = num1//7

        key.draw_key_1(21,count1,num2)


    def _draw_black_keys_2(self,num1,num2,key):
        count1 = num1 // 7

        key.draw_key_2(20, count1, num2)

    def _keystomidi(self, dict ):
        midivalues = []
        for i in range(24,73):
            midivalues.append(i)

        dict = {self.keys[j] : midivalues for j in range(len(self.keys))}



    def _midi_handler(self):

        if self.rt.get_port_count() > 0:
            if self.midi_in.name == "keyboard":
                self.midi_in.close()
                self.midi_in = mido.open_input('Launchkey MK2 49 Launchkey MIDI')
                print(self.midi_in.name)

            else:
                self.midi_open in.receive(block=False)
        elif self.midi_in.closed:
            self.midi_in = mido.open_input('keyboard', virtual=True)
            self.midi_in.receive(block=False))

        else:
            self.midi_in.receive(block=False))











if __name__ == '__main__':
    piano = PyPiano()
    piano.main_loop()