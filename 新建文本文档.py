import turtle
import time

__Pen = turtle.Pen()


__Pen.pendown()
__Pen.speed(200)
for __count in range(90):
    for __count in range(9):
        __Pen.forward(30)
        __Pen.right(40)
    __Pen.right(4)


time.sleep(10)
