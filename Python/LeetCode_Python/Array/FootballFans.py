#!/usr/bin/env python
# coding=utf-8


test = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
[0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
]


def makeAroundXY(x, y):
    return ((x, y - 1),
            (x, y + 1),
            (x - 1 , y),
            (x + 1, y),
            (x - 1, y - 1),
            (x - 1, y + 1),
            (x + 1, y + 1),
            (x + 1, y - 1))


def getFootballFans(court):
    fans_group = []
    x = 0
    y = 0
    x_length = len(court[0])
    y_length = len(court)

    def helper(x, y, result=0):
        nonlocal court
        XY = makeAroundXY(x, y)
        for i in XY:
            try:
                if i[0] < 0 or i[1] < 0:
                    continue

                if court[i[1]][i[0]] == 1:
                    court[i[1]][i[0]] = 0
                    result += 1
                    t = helper(i[0], i[1], 0)
                    result += t
            except IndexError:
                continue
        else:
            return result

    for y in range(y_length):
        for x in range(x_length):
            if court[y][x] == 1:
                court[y][x] = 0
                fans_group.append(helper(x, y, 1))

    if not fans_group:
        return (0, 0)
    return (len(fans_group), max(fans_group))


print(getFootballFans(test))
