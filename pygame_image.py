import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock  = pg.time.Clock()
    bg_img_1 = pg.image.load("fig/pg_bg.jpg")
    bg_img_2 = pg.image.load("fig/pg_bg.jpg")
    bg_img_2 = pg.transform.flip(bg_img_2, True, False)
    koukaton = pg.image.load("fig/3.png")
    koukaton = pg.transform.flip(koukaton, True, False)

    koukaton_lst = [koukaton, pg.transform.rotozoom(koukaton, 20, 1.0) ]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        x = -(tmr % 1600)

        screen.blit(bg_img_1, [x, 0])
        screen.blit(bg_img_2, [1600 + x, 0])

        screen.blit(koukaton_lst[int(tmr / 50 % 2)], [200, 300])

        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
