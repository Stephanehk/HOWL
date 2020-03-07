import sys
import pygame as pg
import os
import time
import timeit

from pyAudioAnalysis import audioTrainTest as aT
from microphone_class import AudioRecorder


def play_music(music_file):
    '''
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    '''
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(music_file)
        print("Music file {} loaded!".format(music_file))
    except pygame.error:
        print("File {} not found! {}".format(music_file, pg.get_error()))
        return

    pg.mixer.music.play()

    while pg.mixer.music.get_busy():
        clock.tick(30)

#initalize speakers
freq = 44100    # audio CD quality
bitsize = -16   # unsigned 16 bit
channels = 2    # 1 is mono, 2 is stereo
buffer = 2048   # number of samples (experiment to get right sound)
pg.mixer.init(freq, bitsize, channels, buffer)
pg.mixer.music.set_volume(0.8)

s = timeit.default_timer()
while True:
    audio_thread = AudioRecorder()
    audio_thread.start("output/","/Desktop")
    e =timeit.default_timer()
    #check time elapsed
    if e-s >= 3:
        s = e
        time.sleep(25)
        audio_thread.stop()
        #classify audio
        out = aT.file_classification("output/current_recording.wav", "svmSMtemp","svm")
        #play recording accordingly
        if int(out[1][0]) == 1:
            play_music("file")
            time.sleep(25)
