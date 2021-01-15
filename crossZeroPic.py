'''if __name__=='__main__':'''
from turtle import *
import cfg


def cross(cell):
    goto(cell[0] * cfg.sizeCell, cell[1] * cfg.sizeCell)  # переходим в центр клетки
    down()
    right(45)
    fd(20)
    bk(40)
    fd(20)
    left(90)
    fd(20)
    bk(40)
    fd(20)
    right(45)
    up()


def circl(cell) -> object:
    goto(cell[0] * cfg.sizeCell, cell[1] * cfg.sizeCell)  # переходим в центр клетки
    down()
    right(90)
    up()
    fd(20)
    down()
    left(90)
    circle(20)
    left(90)
    up()
    fd(20)
    down()
    right(90)
    up()
