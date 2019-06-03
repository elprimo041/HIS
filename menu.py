# -*- coding: utf-8 -*-
from psychopy import visual, event
import tests, intro


def menu(myWin, N, test_num):
    result = []
    #インスタンスを作成
    test = tests.Test(myWin, N)  

    if test_num == 1:
        line1 = u'実験１:単純反応'
    elif test_num == 2:
        line1 = u'実験2:物理的照合'
    elif test_num == 3:
        line1 = u'実験3:名称称号'
    elif test_num == 4:
        line1 = u'実験4:カテゴリ照合'
    
    msg = visual.TextStim(myWin, font = 'ヒラギノ角ゴシック W5', color = 'Black'\
                      , alignHoriz = 'left', alignVert = 'top');
    
    msg.setText(line1 + u'\n\n実験に進む場合は1を,説明を表示するには２を, \
                \n実験選択に戻るにはqを入力してください．\
                \n\n1:実験開始\n\n2:イントロ\n\nq:実験選択に戻る')
    msg.pos = (-0.7, 0.7)
    event.clearEvents()
    while True:
        msg.draw()
        myWin.flip()
        key = event.getKeys()
        if '1' in key:
            if test_num == 1:
                result = test.test1(0, test_num)
            else:
                result = test.test2(0, test_num)
            break
            
        elif '2' in key:
            tmp = intro.intro(myWin, N, test_num)
            if tmp == 0:
                if test_num == 1:
                    result = test.test1(0, test_num)
                else:
                    result = test.test2(0, test_num)
            break
        
        elif 'q' in key:
            return
    return result