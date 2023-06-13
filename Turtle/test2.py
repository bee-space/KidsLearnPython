#!/usr/bin/python3
import turtle

pen=turtle.Pen()

print('Виберіть що хочете намалювати.')

print('квадрат     коло')
picture=input()
if(picture == 'коло'):
    pen.circle(100)
elif(picture == 'квадрат'):
    pen.forward(200)
    pen.left(90)
    pen.forward(200)
    pen.left(90)
    pen.forward(200)
    pen.left(90)
    pen.forward(200)
    pen.left(90)
    pen.forward(200)
else:
    print('я не знаю такої фігури')
    
int(input())