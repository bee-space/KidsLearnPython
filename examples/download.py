#!/usr/bin/python3

import turtle

pen=turtle.Pen()

download=0

while(download <= 3):
    download += 1
    
    if(download == 1):
        pen.begin_fill()
        pen.fillcolor('green')
        pen.circle(75)
        pen.end_fill()
        pen.begin_fill()
        pen.fillcolor('white')
        pen.circle(75)
        pen.end_fill()
        pen.up()
        pen.right(90)
        pen.forward(150)
        pen.left(90)
        pen.down()
    if(download == 2):
        pen.begin_fill()
        pen.fillcolor('yellow')
        pen.circle(75)
        pen.end_fill()
        
        pen.begin_fill()
        pen.fillcolor('white')
        pen.circle(75)
        pen.end_fill()
        
        pen.up()
        pen.right(90)
        pen.forward(150)
        pen.left(90)
        pen.down()
    if download == 3:
        pen.begin_fill()
        pen.fillcolor('red')
        pen.circle(75)
        pen.end_fill()
        
        pen.begin_fill()
        pen.fillcolor('white')
        pen.circle(75)
        pen.end_fill()
        download=0
        
        pen.up()
        pen.left(90)
        pen.forward(300)
        pen.right(90)
        pen.down()
        

print('завантаження завершено')
input()
    