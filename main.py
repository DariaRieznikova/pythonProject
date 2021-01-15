from typing import Dict, Any, Union, Tuple, List
from bob import*
import cfg
from cfg import sizeCell

victory: bool = False
mouseClicked = False  # нажата ли мышка
# bob - robot
up()
goto(0, -25)
down()


def blank(x):
    hideturtle()
    speed(0)
    x_turtle = -x * 1.5
    y_turtle = -x * 1.5
    up()
    goto(x_turtle, y_turtle)
    for count in range(4):
        down()
        goto(x_turtle + 3 * x, y_turtle)
        up()
        y_turtle += x
        goto(x_turtle, y_turtle)
    up()
    y_turtle -= x
    goto(x_turtle, y_turtle)
    for count in range(4):
        down()
        goto(x_turtle, y_turtle - 3 * x)
        up()
        x_turtle += x
        goto(x_turtle, y_turtle)


def mouseClick(x, y):
    global mouseClicked
    if mouseClicked:  # если мышка нажата то выходим
        return
    mouseClicked = True  # мышку нажали
    res: dict = cfg.getResult()
    global victory
    if len(res) > 8 or victory:
        reset()
        res.clear()
        blank(sizeCell)
        bob_cell = bobGo()
        victory = False
    else:
        cell = ((int(x) // (sizeCell // 2) + 1) // 2, (int(y) // (sizeCell // 2) + 1) // 2)
        # переводим координаты щелчка мышкой в номер клетки
        if cell[0] ** 2 < 2 and cell[1] ** 2 < 2 and cell not in res:
            # условие попадание в решотку
            # пустая ли клетка
            if len(res) % 2 == 0:  # нечетный ход
                pass
            else:  # четный ход
                circl(cell)
                res[cell] = -1
                vls: List[Tuple[Tuple[int, int], Tuple[int, int]]] = checkVictory()
                if len(vls) == 0:
                    bob_cell = bobGo()
                    vls = checkVictory()
            if len(vls) > 0:
                victory = True
                up()
                goto(vls[0][0][0] * sizeCell, vls[0][0][1] * sizeCell)
                width(10)
                color('red')
                down()
                goto(vls[0][1][0] * sizeCell, vls[0][1][1] * sizeCell)
    mouseClicked = False  # мышку обработали


def checkVictory():
    vls = []
    res = cfg.getResult()
    for i in range(-1, 2):
        s = sum({k: v for k, v in res.items() if k[0] == i}.values())  # сума по строчкам
        if s == 3 or s == -3:
            vls.append(((i, -1), (i, 1)))
        s = sum({k: v for k, v in res.items() if k[1] == i}.values())  # сума по стовпцям
        if s == 3 or s == -3:
            vls.append(((-1, i), (1, i)))
    s = sum({k: v for k, v in res.items() if k[1] == k[0]}.values())  # сума діагоналі 1
    if s == 3 or s == -3:
        vls.append(((-1, -1), (1, 1)))
    s = sum({k: v for k, v in res.items() if k[1] + k[0] == 0}.values())  # сума діагоналі 2
    if s == 3 or s == -3:
        vls.append(((-1, 1), (1, -1)))
    return vls


if __name__ == '__main__':
    blank(sizeCell)
    bobCell = bobGo()
    onscreenclick(mouseClick)
    done()
