#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from psychopy import visual
from mutagen.mp3 import MP3 as mp3
from statistics import mean
import time
import pygame
import os


base = os.path.dirname(os.path.abspath(__file__))
announce = os.path.normpath(os.path.join(base, r'music/Announce.mp3'))
tin = os.path.normpath(os.path.join(base, r'music/Tin.mp3'))
drum = os.path.normpath(os.path.join(base, r'music/Drum.mp3'))
voice = []
voice.append(os.path.normpath(os.path.join(base, r'music/Excellent.mp3')))
voice.append(os.path.normpath(os.path.join(base, r'music/Great.mp3')))
voice.append(os.path.normpath(os.path.join(base, r'music/Good.mp3')))
voice.append(os.path.normpath(os.path.join(base, r'music/Bad.mp3')))

def main(myWin, test_num, result, error):
    msg1 = visual.TextStim(myWin, font = 'ヒラギノ角ゴシック W5', color = 'Black');
    msg2 = visual.TextStim(myWin, font = 'ヒラギノ角ゴシック W5', color = 'Black');
    msg1.setText('結果発表')
    msg1.pos = (0, 0.6)
    msg2.height = (0.25)
    msg1.draw()   
    myWin.flip()
    pygame.mixer.init()
    pygame.mixer.music.load(announce)
    pygame.mixer.music.play(1)
    time.sleep(3.5)
    pygame.mixer.music.stop()
    time.sleep(0.01)
    
    grade = [[0.225, 0.242, 0.263],\
             [0.265, 0.297, 0.350],\
             [0.288, 0.331, 0.376],\
             [0.306, 0.340, 0.373]]
    
    
    if error == True:
        msg2.setText('ミスが多すぎました')
        msg1.draw()
        msg2.draw()
        myWin.flip()
        pygame.mixer.init()
        pygame.mixer.music.load(tin)
        wait = mp3(tin).info.length
        pygame.mixer.music.play(1)
        time.sleep(wait)
        pygame.mixer.music.stop()
        time.sleep(1)
        
    else:
        if mean(result) < grade[test_num-1][0]:
            msg2.setText('お前がNO.1だ!!')
            index = 0
        elif mean(result) < grade[test_num-1][1]:
            msg2.setText('グレイト！')
            index = 1
        elif mean(result) < grade[test_num-1][2]:
            msg2.setText('合格です！')
            index = 2
        else:
            msg2.setText('残念…\n次は頑張ろう')
            index = 3
            
        msg1.draw()
        msg2.draw()
        myWin.flip()
        pygame.mixer.init()
        pygame.mixer.music.load(voice[index])
        wait = mp3(voice[index]).info.length
        pygame.mixer.music.play(1)
        time.sleep(wait)
        pygame.mixer.music.stop()
        time.sleep(1)