#!/usr/bin/env python
# coding=utf-8
import math
import turtle


def drawCircleTurtle(x, y, r):
    turtle.up()
    turtle.setpos(x + r, y)
    turtle.down()

    for i in range(0, 365, 5):
        a = math.radians(i)
        turtle.setpos(x + r*math.cos(a), y + r*math.sin(a))


def drawSpiralTurtle(x, y, r):
    turtle.up()
    turtle.setpos(x + r, y)
    turtle.down()

    for i in range(0, 360*10, 5):
        a = math.radians(i)
        x = r*math.cos(a)*math.exp(0.05*a)
        y = r*math.sin(a)*math.exp(0.05*a)
        turtle.setpos(x, y)


def main():
    print('Testing...')

    drawCircleTurtle(100, 100, 50)

#    drawSpiralTurtle(0, 0, 5)

    turtle.mainloop()


if __name__ == '__main__':
    main()
