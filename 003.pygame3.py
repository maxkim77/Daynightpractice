import pygame as pg

#import pandas as pd

pg.init()

화면가로길이 = 600
화면세로길이 = 800

화면 = pg.display.set_mode((화면가로길이, 화면세로길이))

#창이름 배경추가하기
pg.display.set_caption('생선잡기_게임')

배경이미지 = pg.image.load("img/배경.png")
배경이미지 = pg.transform.scale(배경이미지, (화면가로길이, 화면세로길이))
화면.blit(배경이미지, (0,0))

물고기1 = pg.image.load("img/물고기1.png")
물고기1 = pg.transform.scale(물고기1, (64, 64))
화면.blit(물고기1, (100, 400))

물고기2 = pg.image.load("img/물고기2.png")
물고기2 = pg.transform.scale(물고기2, (64, 64))
화면.blit(물고기2, (200, 300))

스코어바 = pg.image.load("img/스코어바.png")
스코어바 = pg.transform.scale(스코어바, (250, 74))
화면.blit(스코어바, (350, 2))

시간바 = pg.image.load("img/시간-바.png")
시간바 = pg.transform.scale(시간바, (200, 55))
화면.blit(시간바, (0, 10))

pg.draw.line()
pg.display.update()

폰트 = pg.font.SysFont('hy얕은샘물m', 30, True)
시작시간 = pg.time.get_ticks()
잡은물고기 = 0 

while True:
    경과시간 = round((pg.time.get_ticks() - 시작시간)/1000,1)
    화면.blit(시간바, (0,10))
    화면.blit(스코어바, (350,2))
    
    시간 = 폰트.render(f'{경과시간} 초', True, (0,0,0))
    화면.blit(시간, (60, 28))

    물고기점수 = 폰트.render(f'{잡은물고기} 마리', True, (0,0,0))
    화면.blit(물고기점수, (450, 28))

    pg.display.update()

    for 이벤트 in pg.event.get():
        if 이벤트.type == pg.QUIT:
            quit()
