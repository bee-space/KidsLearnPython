from turtle import *

bgcolor("black")
t = Turtle()
t.pencolor("green")
t.speed(0)
t.left(1)
print(11%10)

c = 0;
for i in range(700):
    t.circle(190-c, 90)
    t.left(120)
    if(i%10==0):
        c=c+1;
    if(i>100):
        t.pencolor("red")
    if(i>200):
        t.pencolor("blue")
    if(i>300):
        t.pencolor("green")
    if(i>400):
        t.pencolor("yellow")
    if(i>500):
        t.pencolor("red")

mainloop()