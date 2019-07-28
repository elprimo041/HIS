# -*- coding: utf-8 -*-
import pygame
import sys, random, csv
from pygame.locals import *


(w,h) = (1200,900)   # 画面サイズ
(x,y) = (w/2, h/2)
pygame.init()       # pygame初期化
pygame.display.set_mode((w, h), 0, 32)  # 画面設定
pygame.display.set_caption("Report3")
msg_font = pygame.font.SysFont(None, 80)     # msgフォントの作成
screen = pygame.display.get_surface()
D = 4   # ターゲットまでの距離
W = 2   # ターゲットの幅
N = 20   # 実験回数

def start():   
    start_msg = msg_font.render(u'Press H key to start', True, (0,0,0))
    x = (w - start_msg.get_width()) / 2
    y = (h - start_msg.get_height()) / 5
    flag = False
    while flag == False:        
        screen.blit(start_msg, (x, y))
        pygame.display.update()     # 画面更新
        pygame.time.wait(30)        # 更新時間間隔
        screen.fill((255,255,255))  # 画面の背景色
        # イベント処理
        i = 0
        for event in pygame.event.get():
            i += 1
            # 画面の閉じるボタンを押したとき
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # キーを押したとき
            if event.type == KEYDOWN:
                # ESCキーなら終了
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_h:
                    flag = True
                    
def test():
    mark_font = pygame.font.SysFont(None, 1000)     # markフォントの作成
    result = []
    left_keys = [K_g, K_f, K_d, K_s, K_a]
    right_keys = [K_j, K_k, K_l, K_SEMICOLON, K_QUOTE]
    left = []
    right = []
    for i in range(W):    
        left.append(left_keys[D+i-1])
        right.append(right_keys[D+i-1])
    
    alert_msg = msg_font.render(u'Keep pressing H key', True, (0,0,0))
    alert_x = (w - alert_msg.get_width()) / 2
    alert_y = (h - alert_msg.get_height()) / 5
    
    mark_R = mark_font.render(u'>', True, (255,0,0))
    R_x = (w - mark_R.get_width()) / 2 + (w - mark_R.get_width()) / 3
    R_y = (h - mark_R.get_height()) / 2
    
    mark_L = mark_font.render(u'<', True, (255,0,0))
    L_x = (w - mark_L.get_width()) / 2 - (w - mark_R.get_width()) / 3
    L_y = (h - mark_L.get_height()) / 2
    
    while len(result) < N:
        flag = False
        wait = random.randint(1000, 3000)
        lr = random.random()
        
        while True:
            pygame.event.pump()
            key = pygame.key.get_pressed()
            screen.blit(alert_msg, (alert_x, alert_y))
            pygame.display.update()     # 画面更新
            pygame.time.wait(30)        # 更新時間間隔
            screen.fill((255,255,255))  # 画面の背景色
            if key[K_h]:
                break      
            
        start = pygame.time.get_ticks()
        
        while pygame.time.get_ticks() - start < wait:
            pygame.event.pump()
            key = pygame.key.get_pressed()       
            if key[K_h] == False:
                screen.blit(alert_msg, (alert_x, alert_y))
            pygame.display.update()     # 画面更新
            pygame.time.wait(30)        # 更新時間間隔
            screen.fill((255,255,255))  # 画面の背景色
            
        pygame.event.clear()    
        start = pygame.time.get_ticks()
#        roop = []
        while flag == False:
#            if len(roop) < 1000:
#                roop.append(pygame.time.get_ticks() - start)
            pygame.event.pump()
            key = pygame.key.get_pressed()       
            if key[K_h]:
                key_up = pygame.time.get_ticks() - start
            if lr < 0.5:
                screen.blit(mark_L, (L_x, L_y))
            else:
                screen.blit(mark_R, (R_x, R_y))   
            pygame.display.update()     # 画面更新
            screen.fill((255,255,255))  # 画面の背景色
                
            # イベント処理
            for event in pygame.event.get():
                # キーを押したとき
                if event.type == KEYDOWN:
                    stop = pygame.time.get_ticks() - start
                    flag = True
                    if event.key in left and lr < 0.5:
                        result.append([key_up, stop])                      
                    elif event.key in right and lr >= 0.5:
                        result.append([key_up, stop])
#    
#    with open('roop.csv', 'w') as f:
#        writer = csv.writer(f)
#        for i in range(len(roop)):
#            writer.writerow([roop[i]])               
    return result
    
    
            
def main():
    start()
    result = test()
    filename = 'result_' + str(D) + '_' + str(W) + '.csv'
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for i in range(len(result)):
            writer.writerow(result[i])
    

            

if __name__ == '__main__':
    main()