# -*- coding: utf-8 -*-
from psychopy import visual, event
import tests

def intro(myWin, N, test_num):
    #インスタンスを作成
    test = tests.Test(myWin, N)
    msg = visual.TextStim(myWin, font = 'ヒラギノ角ゴシック W5', color = 'Black'\
                      , alignHoriz = 'left', alignVert = 'top');
    
    if test_num == 1:
        text = u'実験１:単純反応\tイントロ\
                \n\n画面上にランダムなアルファベットが表示されます.\
                \n表示されたらできるだけ早く任意のキーを押してください.\
                \n練習画面に進むには1を,\n実験に進むには２を入力してください.\
                \n\n1:練習\n\n2:実験\n\nq:実験選択に戻る'
    elif test_num == 2:
        text = u'実験2:物理的照合\tイントロ\
                \n\n画面左側にアルファベットが表示されます.\
                \nその後右側にもアルファベットが表示されます.\
                \n左右に表示された文字が物理的に一致していたらスペースを,\
                \n一致していなければ何も押さず待機してください.\
                \n※大文字と小文字は区別します\
                \n※誤答率が３割を超えると結果が保存されません\
                \n\n例: AA → スペース(一致)\
                \n　  AB → エンター(不一致)\
                \n　  Aa → エンター(不一致)\
                \n\n練習画面に進むには1を,\
                \n実験に進むには２を\
                実験選択に戻るにはqを入力してください.\
                \n\n1:練習\n\n2:実験\n\nq:実験選択に戻る'
    elif test_num == 3:
        text = u'実験3:名称称号\tイントロ\
                \n\n画面左側にアルファベットが表示されます.\
                \nその後右側にもアルファベットが表示されます.\
                \n左右に表示された文字の名称が一致していたらスペースを,\
                \n一致していなければ何も押さず待機してください.\
                \n※大文字と小文字は区別しません\
                \n※誤答率が３割を超えると結果が保存されません\
                \n\n例: AA → スペース(一致)\
                \n　  AB → エンター(不一致)\
                \n　  Aa → スペース(一致)\
                \n\n練習画面に進むには1を,\
                \n実験に進むには２を\
                実験選択に戻るにはqを入力してください.\
                \n\n1:練習\n\n2:実験\n\nq:実験選択に戻る'
    elif test_num == 4:
        text = u'実験4:カテゴリ照合\tイントロ\
                \n\n画面左側に文字が表示されます.\
                \nその後右側にも文字が表示されます.\
                \n左右に表示された文字のカテゴリが一致していたらスペースを,\
                \n一致していなければ何も押さず待機してください.\
                \n※カテゴリ:大文字,小文字,数字\
                \n※誤答率が３割を超えると結果が保存されません\
                \n\n例: AR → スペース(一致)\
                \n　  Ab → エンター(不一致)\
                \n　  A3 → スペース(一致)\
                \n\n練習画面に進むには1を,\
                \n実験に進むには２を\
                実験選択に戻るにはqを入力してください.\
                \n\n1:練習\n\n2:実験\n\nq:実験選択に戻る'
    
    msg.pos = (-0.95, 0.9)
    msg.height = 0.08
    msg.setText(text)
    msg.draw()
    myWin.flip()    
    while True:
        key = event.getKeys()
        if '1' in key:
            if test_num == 1:
                test.test1(3, test_num)
            else:
                test.test2(3, test_num)
            msg.setText('練習を終了します.\n実験を始めるには１を,\
                        実験選択に戻るにはqを入力してください.\
                        \n\n1:実験\n\nq:実験選択に戻る')
            msg.pos = (-0.7, 0.7)
            msg.draw()
            myWin.flip()
            while True:
                key = event.getKeys()
                if '1' in key:
                    break
                if 'q' in key:
                    return
            break
        
        elif '2' in key:
            break
        
        elif 'q' in key:
            return
    
    return 0