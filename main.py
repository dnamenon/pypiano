import sys


import tkinter
from tkinter import *
import mido
from mido import messages
import rtmidi
import os
import tracemalloc
import asyncio
import simpleaudio as sa

from settings import Settings
from white_keys import White_Key
from black_keys import Black_Key





class PyPiano:
    """overall class to manage game assets and behavior"""

    def __init__(self):



        gui = tkinter.Tk()
        tracemalloc.start()

        self.settings = Settings()

        self.screen = Canvas(gui, width=self.settings.screen_width, height=self.settings.screen_height, bg =self.settings.bg_color)
        self.screen.config(scrollregion=self.screen.bbox(ALL))
        self.screen.pack()



        self.rt = rtmidi.MidiIn()

        if self.rt.get_port_count() != 0:
            self.midi_in = mido.open_input('Launchkey MK2 49 Launchkey MIDI')
        else:
            self.midi_in = mido.open_input('keyboard', virtual=True)
        self.midi_in.receive(block=False)


        self.keys = []
        self._make_keys()
        self._assign_audiofiles()


        self.key_midi = {}
        self._keystomidi()


        self._draw_keys()

        gui.mainloop()


    def main(self):
        self._midi_handler()





    def _event_handler(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                del self.midi_in
                sys.exit()

    def _make_keys(self):

        for value in range(1,30):

            self.keys.append(White_Key(self))


            if (value % 7 == 1 or value % 7 == 2 or value % 7 == 4 or value % 7 == 5 or value % 7 == 6) and value < 29:
                #the extra c on top shouldn't have a black key assigned to it
                self.keys.append(Black_Key(self))


    def _draw_keys(self):
        count = 0
        count2 = 1
        count3 = 1


        for key in self.keys:
            if type(key) is White_Key:
                key.draw_key((count)*35)
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


    def _keystomidi(self):
        midivalues = []
        for i in range(24,73):
            midivalues.append(i)

        self.key_midi = {midivalues[j] : self.keys[j] for j in range(len(self.keys))}

    def _message_handler(self):

        for msg in self.midi_in:
            print(msg)
            key = self.key_midi[int(msg.note)]

            wave_obj = sa.WaveObject.from_wave_file(f"piano_samples/{key.note_value}")
            play_obj = wave_obj.play()
            play_obj.wait_done()




    def _assign_audiofiles(self):
        filenames = []

        for filename in os.listdir("piano_samples"):
            if filename.endswith(".wav"):

                filenames.append(filename)
        filenames.sort()

        for i in range(0,49):
            self.keys[i].assign_note_value(filenames[i])

    def _midi_handler(self):

        if self.rt.get_port_count() > 0:
            #these statements handle when the midi device is plugged in or out when the program is running
            if self.midi_in.name == "keyboard": # in case t
                self.midi_in.close() #close keyboard midi so only one port is open

                self.midi_in = mido.open_input('Launchkey MK2 49 Launchkey MIDI')
                self.midi_in.receive(block=False)
                # will need to adjust later to handle other types of midi devices

                print(self.midi_in.name)
                self._message_handler()

            else:

                self._message_handler()


        elif self.midi_in.closed:

            self.midi_in = mido.open_input('keyboard', virtual=True)
            print(self.midi_in.name)
            self.midi_in.receive(block=False)
            self._message_handler()

        else:
            self._message_handler()






if __name__ == '__main__':
    piano = PyPiano()
    piano.main()