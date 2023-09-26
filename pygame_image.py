import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    koukaton = pg.image.load("fig/3.png")
    koukaton = pg.transform.flip(koukaton, True, False)
    koukaton_routed = pg.transform.rotozoom(koukaton, 10, 1.0)

    koukaton_lst = [koukaton, koukaton_routed]

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        x = -(tmr % 1600)

        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img, [1600 + x, 0])
        screen.blit(koukaton_lst[tmr%2],[200, 300])
        pg.display.update()
        tmr += 1        
        clock.tick(1000000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
