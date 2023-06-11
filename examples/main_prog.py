#!/usr/bin/python3
import math
import Pen
import Say
import base

#def імя_функції([параметри]):
#    інструкції або код

def say_hello():
    print("Hello Misha")
    print("Hello Sasha")

def say(name):
    print('hello, ' + name)

def plus(a, b):
    print('Додавання двух чисел:')
    print(a + b)

def plus(a, b):
    print('Додавання двух чисел:')
    print(a + b)

def wl(number):
    while number > 0:
        print(" * " * number)
        number -= 1
    print("цикли завершено")
    print("number = " + str(number))
    
def sum(a, b):
    s = a + b
    return s

def pifagor(cat1, cat2):
    return math.sqrt(cat1*cat1 + cat2*cat2)
    

print('Привіт, функції і методи')

a = sum(10, 20) #30 
b = sum(5, 10) #15
c = sum(a, b) #30+15 = 45
#print(c)
#print(pifagor(10, 30))

print(base.check_user_mail('sychov.s@gmail.com'))
print(base.check_user_mail('s.sychov@gmail.com'))

print(base.check_user_name('Misha Tovstenko'))

print(base.check_user_name('Serhii Sychov'))

#Pen.sq(200)
#Pen.sqr(300,400)

#Say.Hello('DOG')
#Say.Bay('DOG')

#wl(30)

#say_hello()
#say('Misha')
#say('Sasha')
#say('dog')

#plus(10,10)
#plus(12,12)
#plus(124,120)
#plus(5475758,5454)




