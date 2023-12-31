import sys
import pygame as pg
import random




WIDTH, HEIGHT = 1600, 900
delta = {
        pg.K_UP: (0,-5),
        pg.K_DOWN: (0,+5),
        pg.K_LEFT: (-5,0),
        pg.K_RIGHT: (+5,0)
        }


def check_bound(obj_rct: pg.Rect):
    yoko,tate = True,True
    if obj_rct.left < 0 or WIDTH < obj_rct.right:
        yoko = False
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom:
        tate = False
    return yoko,tate


def kk_k():
    kk_img0 = pg.transform.rotozoom(pg.image.load("ex02/fig/3.png"), 0, 2.0)
    kk_img1 = pg.transform.flip(kk_img0, True, False)
    return{
        (0, 0):kk_img0,
        (-5, 0):kk_img0,
        (-5, -5):pg.transform.rotozoom(kk_img0, -45, 1.0),
        (-5, +5):pg.transform.rotozoom(kk_img0, 45, 1.0),
        (0, -5):pg.transform.rotozoom(kk_img1, 90, 1.0),
        (+5, -5):pg.transform.rotozoom(kk_img1, 45, 1.0),
        (+5, 0):pg.transform.rotozoom(kk_img1, 0, 1.0),
        (+5, +5):pg.transform.rotozoom(kk_img1, -45, 1.0),
        (0, +5):pg.transform.rotozoom(kk_img1, -90, 1.0)
        }


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_imgs = kk_k()
    kk_img = kk_imgs[(0,0)]

    kk_rct = kk_img.get_rect()
    kk_rct.center = 900,400


    bb_img = pg.Surface((20,20))
    pg.draw.circle(bb_img,(255,0,0),(10,10),10)
    bb_img.set_colorkey((0,0,0))
    bb_rct = bb_img.get_rect()
    bb_rct.centerx = random.randint(0,WIDTH)
    bb_rct.centery = random.randint(0,HEIGHT)
    vx, vy = +10, +10

    saccs = [a for a in range(1, 11)]



    clock = pg.time.Clock()
    tmr = 0


    accs = [a for a in range(1,11)]
    if tmr == 10*accs[1]:
        vx, vy = +10, +10


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
       
        if kk_rct.colliderect(bb_rct):
            print("Game Over")
            return
           
        key_lst =pg.key.get_pressed() #ps.key.get_pressed()で取得したkey_lstを使用しての動作のプログラム
        if key_lst[pg.K_UP]: #Key_lst内のK_UPが押されたとき
            kk_img = kk_imgs[(0,-5)] #kk_imgをkk_imgs[(0,5)]に変更する
        if key_lst[pg.K_DOWN]:
            kk_img = kk_imgs[(0,+5)]
        if key_lst[pg.K_LEFT]:
            kk_img = kk_imgs[(-5,0)]
            if key_lst[pg.K_UP]:
                kk_img = kk_imgs[(-5,-5)]
            if key_lst[pg.K_DOWN]:
                kk_img = kk_imgs[(-5,+5)]
        if key_lst[pg.K_RIGHT]:
            kk_img = kk_imgs[(+5,0)]
            if key_lst[pg.K_UP]:
                kk_img = kk_imgs[(+5,-5)]
            if key_lst[pg.K_DOWN]:
                kk_img = kk_imgs[(+5,+5)]

        sum_mv=[0,0]
        for k, tpl in delta.items():
            if key_lst[k]:
                sum_mv[0] += tpl[0]
                sum_mv[1] += tpl[1]


        screen.blit(bg_img, [0, 0])
        kk_rct.move_ip(sum_mv[0],sum_mv[1])
        if check_bound(kk_rct) != (True, True):
            kk_rct.move_ip(-sum_mv[0], -sum_mv[1])
        screen.blit(kk_img, kk_rct)
        screen.blit(bb_img,bb_rct)
        bb_rct.move_ip(vx, vy)
        yoko,tate = check_bound(bb_rct)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        pg.display.update()
        tmr += 1
        clock.tick(50)




if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
