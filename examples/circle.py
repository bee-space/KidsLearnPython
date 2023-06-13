#!/usr/bin/python3

import turtle

pen=turtle.Pen()

pen.circle(50)

print('виберіть наскільки пікселів напрям і градус куди хочете перемістити коло')

print('впишіть напрям')

direction=input()

print('кількість пікселів')

pixel=int(input())

print('градуси')

degree=int(input())

print('маштаб кола')

scale=int(input())

if(direction=='вліво'):
    pen.reset()
    pen.up()
    pen.left(degree)
    pen.forward(pixel)
    pen.down()
    pen.circle(scale)


elif(direction=='вправо'):
    pen.reset()
    pen.up()
    pen.right(degree)
    pen.forward(pixel)
    pen.down()
    pen.circle(scale)
else:
    print('я вас нерозумію')

