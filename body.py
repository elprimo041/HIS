# -*- coding: utf-8 -*-
from psychopy import visual, event
import menu
import time
import os

#1回の実験あたりの試行回数
N = int(input('1回の実験あたりの試行回数:'))
ID = input('ID:')

total_result = []
hist = []
test_list = [u'単純反応', u'物理的照合', u'名称称号', u'カテゴリ照合']
myWin = visual.Window(units='norm', size=(1200, 900), color=[1,1,1])
msg = visual.TextStim(myWin, font = 'ヒラギノ角ゴシック W5', color = 'Black'\
                      , alignHoriz = 'left', alignVert = 'top')


top = u'実行する実験番号を入力してください.\
     \n終了する場合はqを入力してください.\
     \n\n1:' + test_list[0] + '\n\n2:' + test_list[1]+ '\n\n3:'\
     + test_list[2]+ '\n\n4:' + test_list[3] + '\n\nq:終了'

event.clearEvents()
while True:
    msg.setText(top)
    msg.pos = (-0.7, 0.7)
    msg.draw()
    myWin.flip()
    key = event.getKeys()
    if '1' in key:
        myWin.flip()
        tmp = menu.menu(myWin, N, 1)
        if type(tmp) is list and len(tmp) != 0:
            hist.append(1)
            total_result.append(tmp)
        
    elif '2' in key:
        myWin.flip()
        tmp = menu.menu(myWin, N, 2)
        if type(tmp) is list and len(tmp) != 0:
            hist.append(2)
            total_result.append(tmp)
        
    elif '3' in key:
        myWin.flip()
        tmp = menu.menu(myWin, N, 3)
        if type(tmp) is list and len(tmp) != 0:
            hist.append(3)
            total_result.append(tmp)
        
    elif '4' in key:
        myWin.flip()
        tmp = menu.menu(myWin, N, 4)
        if type(tmp) is list and len(tmp) != 0:
            hist.append(4)
            total_result.append(tmp)

    elif 'q' in key:
        myWin.flip()
        msg.alignHoriz = 'center'
        msg.alignVert = 'center'
        msg.setText(u'プログラムを終了します.')      
        msg.pos = (-0, 0)
        msg.draw() 
        myWin.flip()
        time.sleep(0.2)
        break


for i in range(len(hist)):
    base = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.normpath(os.path.join(base, r'result/row_data/' + ID + '_test' + str(hist[i]) + '.csv'))
    if hist[i] == 1:
        with open(file_name, 'a') as f:
            for j in range(N):
                print(total_result[i][j], file=f)
                
    elif hist[i] == 2:
        with open(file_name, 'a') as f:
            for j in range(N):
                print(total_result[i][j], file=f)
                
    elif hist[i] == 3:
        with open(file_name, 'a') as f:
            for j in range(N):
                print(total_result[i][j], file=f)
                
    elif hist[i] == 4:
        with open(file_name, 'a') as f:
            for j in range(N):
                print(total_result[i][j], file=f)
                             

myWin.close()