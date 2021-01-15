from random import *
from crossZeroPic import *
import cfg


# квартира Боба
# bob ходит на нечетных ходах

def bobGo(is_cross=True):
    res = cfg.getResult()

    if len(res) == 0:  # перший хід
        cell = choice([(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1)
                       if x == y or x == -y])  # diagonal
    else:  # не перший хід
        cell = getBobCell(res.copy())
    cross(cell) if is_cross else circl(cell)
    if is_cross :
        res[(cell)] = 1
    else :
        res[(cell)] = -1
    return cell


def getBobCell(res):
    cell = choice([(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1)
                   if (x, y) not in res])
    return cell


def doNotMiss(res):
    vls = []
    res = cfg.getResult()
    for i in range(-1, 2):
        s = sum({k: v for k, v in res.items() if k[0] == i}.values())  # сума по стовпцях
        if s == 2:
            vls.append(((i, -1), (i, 1)))
        s = sum({k: v for k, v in res.items() if k[1] == i}.values())  # сума по строчках
        if s == 2:
            vls.append(((-1, i), (1, i)))
    s = sum({k: v for k, v in res.items() if k[1] == k[0]}.values())  # сума діагоналі /
    if s == 2:
        vls.append(((-1, -1), (1, 1)))
    s = sum({k: v for k, v in res.items() if k[1] + k[0] == 0}.values())  # сума діагоналі \
    if s == 2:
        vls.append(((-1, 1), (1, -1)))
