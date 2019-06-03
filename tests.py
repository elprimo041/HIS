# -*- coding: utf-8 -*-
from psychopy import visual, core, event
import random
import time
import pygame
import evaluate
import os


lower = 'abdefghmnqrt'
upper = 'ABDEFGHMNQRT'
digit = '2345678'
base = os.path.dirname(os.path.abspath(__file__))
start = os.path.normpath(os.path.join(base, r'music/Start.mp3'))
correct_s = os.path.normpath(os.path.join(base, r'music/Correct.mp3'))
wrong = os.path.normpath(os.path.join(base, r'music/Wrong.mp3'))


class Test:
    def __init__(self, myWin, N):
        self.N = N;
        self.myWin = myWin;
        self.msg = visual.TextStim(myWin, font = 'ヒラギノ角ゴシック W5', color = 'Black'\
                      , alignHoriz = 'left', alignVert = 'top');
        self.test_ch1 = visual.TextStim(myWin, font = 'ヒラギノ角ゴシック W5', color = 'Black');
        self.test_ch2 = visual.TextStim(myWin, font = 'ヒラギノ角ゴシック W5', color = 'Black');
        self.mb = visual.TextStim(myWin, font = 'ヒラギノ角ゴシック W5', color = 'Red', bold = True);
        self.counter = visual.TextStim(myWin, font = 'ヒラギノ角ゴシック W5', color = 'Black');
        self.eval = visual.TextStim(myWin, font = 'ヒラギノ角ゴシック W5', color = 'Red');
        self.change = visual.TextStim(myWin, font = 'ヒラギノ角ゴシック W5', color = 'Red');
        self.msg.pos = (-0.7, 0.7)
        self.test_ch1.height = 0.7
        self.test_ch2.height = 0.7
        self.test_ch1.pos = (-0.3, 0)
        self.test_ch2.pos = (0.3, 0)
        self.mb.pos = (0.3, 0.1)
        self.mb.height = 1.2
        self.counter.pos = (0, -0.2)
        self.eval.pos = (0.5, 0.3)
        self.eval.height = 0.2
        self.eval.ori = 30
        self.change.pos = (0, 0.2)
        self.change.height = 0.2
        self.change.ori = 30
        self.change.setText('変更!')
        
    
    def test1(self, inp, test_num):
        #単純反応
        if inp != 0:
            n = inp
        else:
            n = self.N
        result = []
        wait = 0
        self.msg.setText(u'文字が表示されたら何かボタンを押してください.')
        self.msg.alignHoriz = 'center'
        self.msg.alignVert = 'center'
        self.msg.pos = (0, 0.7)
        self.test_ch1.pos = (0, -0.1)
        self.eval.pos = (0.3, 0.2)
        
        t = 3.0
        startClock = core.Clock()
        pygame.mixer.init()
        pygame.mixer.music.load(start)
        pygame.mixer.music.play(1)        
        while t >= 0.2:
            t = 3.6 - startClock.getTime()
            self.msg.draw()
            self.counter.setText('%.0f' % (t))
            self.counter.draw()
            self.myWin.flip()
        self.myWin.flip()
        time.sleep(1.5)
        pygame.mixer.music.stop()
        time.sleep(0.01)
        
        for i in range(n):
            self.myWin.flip()
            wait = random.uniform(1, 3)
            time.sleep(wait)
            self.test_ch1.setText(random.choice(upper))
            event.clearEvents()
            testClock = core.Clock()
            while True:
                self.test_ch1.draw()
                self.myWin.flip()
                key = event.getKeys()
                if len(key) > 0:
                    result.append(testClock.getTime())
                    self.sound(1, 0, result[-1])
                    break
        
      
        event.clearEvents()
        self.myWin.flip()
        self.msg.alignHoriz = 'left'
        self.msg.alignVert = 'top'
        self.msg.pos = (-0.7, 0.7)
        self.eval.pos = (0.7, 0.2)
        evaluate.main(self.myWin, test_num, result, False)
        return result
       
        
    def test2(self, inp, test_num):
        #物理的照合
        #名称称号
        #カテゴリ照合
        if inp != 0:
            n = inp
        else:
            n = self.N
        target = [u'が物理的に', u'の名称が', u'のカテゴリが']
        result = []
        wait = 0
        self.msg.setText(u'左側に表示された文字と右側に表示された\
                         文字' + target[test_num - 2] + '同じならスペースを,\
                         異なるなら何も押さず待機してください.\
                         左側の文字は１０回ごとに変更されます')
        self.msg.pos = (-0.9, 0.7)
        t = 3.0
        startClock = core.Clock()
        pygame.mixer.init()
        pygame.mixer.music.load(start)
        pygame.mixer.music.play(1)        
        while t >= 0.2:
            t = 3.6 - startClock.getTime()
            self.counter.setText('%.0f' % (t))
            self.msg.draw()
            self.counter.draw()
            self.myWin.flip()
        self.myWin.flip()
        time.sleep(1.5)
        pygame.mixer.music.stop()
        time.sleep(0.01)
        
        i = 0
        error = 0
        is_error = False
        left_char = ''
        right_char = ''
        while i < n:
            left_char, right_char, is_correct = self.get_char(test_num, i, left_char, is_error)             
            self.test_ch1.setText(left_char)
            self.test_ch2.setText(right_char)
            self.test_ch1.draw()
            if i % 10 == 0 and i != 0 and is_error == False:
                self.change.draw()
                self.myWin.flip()
                time.sleep(1.5)
                self.test_ch1.setText(left_char)
                self.test_ch1.draw()
            self.myWin.flip()
            wait = random.uniform(1, 1.5)
            self.test_ch1.draw()
            self.test_ch2.draw()
            time.sleep(wait)
            self.myWin.flip()
            event.clearEvents()
            testClock = core.Clock()
            while True:
                key = event.getKeys()
                if 'space' in key and is_correct == True:
                    result.append(testClock.getTime())
                    self.sound(2, 0, result[-1])
                    is_error = False
                    i += 1
                    break
                elif 'space' in key and is_correct == False:
                    self.sound(2, 1, 0)
                    is_error = True
                    error += 1
                    break
                elif testClock.getTime() > 1.5 and is_correct == True:
                    self.sound(2, 1, 0)
                    is_error = True
                    error += 1
                    break
                elif testClock.getTime() > 1.5 and is_correct == False:
                    is_error = True
                    break
                    
        self.msg.pos = (-0.7, 0.7)
        if inp != 0:
            return
        
        elif error/n < 0.3:
            evaluate.main(self.myWin, test_num, result, False)
            return result
        else:
            evaluate.main(self.myWin, test_num, result, True)
            return
        
    def sound(self, test_num, correct, t):
        wait = 2
        grade = [[0.24, 0.253, 0.286],\
                 [0.344, 0.436, 0.53],\
                 [0.1, 0.2, 0.3],\
                 [0.1, 0.2, 0.3]]
        
        if correct == 0:
            if t < grade[test_num-1][0]:
                self.eval.setText('Excellent!')
            elif t < grade[test_num-1][1]:
                self.eval.setText('Great!')
            elif t < grade[test_num-1][2]:
                self.eval.setText('Good!')           
            else:
                self.eval.setText('Bad')
            
            if test_num != 1:
                self.test_ch1.draw()
                self.test_ch2.draw()
                self.eval.draw()
                self.myWin.flip()
                time.sleep(1)
            
            else:
                self.test_ch1.draw()
                self.eval.draw()
                self.myWin.flip()
                time.sleep(1)
            
        elif correct == 1:
            self.mb.setText('×')
            self.test_ch1.draw()
            self.test_ch2.draw()
            self.mb.draw()
            self.myWin.flip()
            pygame.mixer.init()
            pygame.mixer.music.load(wrong)
            pygame.mixer.music.play(1)
            time.sleep(wait)
            pygame.mixer.music.stop()
            time.sleep(0.1)
        
    def get_char(self, test_num, i, a, is_error):
        correct = 0.6
        
        if test_num == 2:
            if i % 10 == 0 and is_error == False:           
                a = random.choice(upper + lower)
            if random.random() < correct:
                is_correct = True
                b = a
            else:
                is_correct = False
                while True:
                    b = random.choice(upper + lower)
                    if a != b:
                        break
        
        elif test_num == 3:
            if i % 10 == 0 and is_error == False:
                a = random.choice(upper + lower)
            if random.random() < correct:
                is_correct = True
                if random.random() < 0.5:
                    b = a
                else:
                    b = str.swapcase(a)
                    
            else:
                is_correct = False
                while True:
                    b = random.choice(upper + lower)
                    if b != a and b != str.swapcase(a):
                        break
                
        elif test_num == 4:
            if i % 10 == 0 and is_error == False:
                code = random.randint(0, 2)
                if code == 0:
                    a = random.choice(lower)
                elif code == 1:
                    a = random.choice(upper)
                elif code == 2:
                    a = random.choice(digit)
            
            if random.random() < correct:
                is_correct = True
                if a in lower:
                    b = random.choice(lower)
                elif a in upper:
                    b = random.choice(upper)
                elif a in digit:
                    b = random.choice(digit)
            else:
                is_correct = False
                if a in lower:
                    b = random.choice(upper + digit)
                elif a in upper:
                    b = random.choice(lower + digit)
                elif a in digit:
                    b = random.choice(upper + lower)
        
        return a, b, is_correct
            
