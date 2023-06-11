#!/usr/bin/python3
import turtle

pen = turtle.Pen()

def sq(a):
    pen.forward(a)
    pen.left(90)
    pen.forward(a)
    pen.left(90)
    pen.forward(a)
    pen.left(90)
    pen.forward(a)
    pen.left(90)
    pen.forward(a)

def sqr(a, b):
    pen.forward(a)
    pen.left(90)
    pen.forward(b)
    pen.left(90)
    pen.forward(a)
    pen.left(90)
    pen.forward(b)
    pen.left(90)
    pen.forward(a)