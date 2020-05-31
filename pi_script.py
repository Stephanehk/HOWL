import sys
import pygame as pg
import os
import time
import timeit
import subprocess
import signal

from pyAudioAnalysis import audioTrainTest as aT

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


def record_sound():
    #proc_args = ['arecord', '-D' , 'dmic_sv' , '-c2' , '-r' , '44100' , '-f' , 'S32_LE' , '-t' , 'wav' , '-V' , 'mono' , '-v' , 'subprocess1.wav']
    proc_args = ['arecord', '-D' , 'plughw:1' , '-c1' , '-r' , '44100' , '-f' , 'S16_LE' , '-t' , 'wav' , '-V' , 'mono' , '-v' , 'recorded_sound.wav']
    rec_proc = subprocess.Popen(proc_args, shell=False, preexec_fn=os.setsid)
    # print("startRecordingArecord()> rec_proc pid= " + str(rec_proc.pid))
    # print("startRecordingArecord()> recording started")
    time.sleep(3)
    os.killpg(rec_proc.pid, signal.SIGTERM)
    rec_proc.terminate()
    rec_proc = None
    #print("stopRecordingArecord()> Recording stopped")


#initalize speakers
freq = 44100    # audio CD quality
bitsize = -16   # unsigned 16 bit
channels = 2    # 1 is mono, 2 is stereo
buffer = 2048   # number of samples (experiment to get right sound)
pg.mixer.init(freq, bitsize, channels, buffer)
pg.mixer.music.set_volume(0.8)

def main():
    #check time elapsed
    record_sound()
    out = aT.file_classification("recorded_sound.wav", "svmSMtemp","svm")
    #play recording accordingly
    if out[1][0] >= 0.5:
        play_music("playback_sound.wav")
        print ("detected coyote howl")
