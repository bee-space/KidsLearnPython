#!/usr/bin/python3 

def cosmos():

    print('Бажаєте пройти наш тест?')    

    print('Напишіть так, або ні')                            
    
    test=input()

    if(test=='так'):
            print('Добре, тоді продовжемо')
    elif(test=='ні'):
        print('Добре, допобачення')
    else:
        print('Я вас не розумію')
    _bal=0
    print('Скільки планет у сонячній системі?')
    print('1   4   8   9')
    plenet=int(input())
    if(plenet==8):
        print('Відповідь вірна')
        _bal=_bal+1
    elif(cosmos==9):
        print('Якщо враховувати плутон тоді так, але плутон вже не рахуєтся як планета')
        _bal=_bal+1
    elif(plenet==1 or plenet==4):
        print('Віповідь не вірна')
    else:
        print('Я вас не розумію')
    print('Скільки супутників має сатурн?')
    print('4   82   102   46')
    saturn=int(input())
    if(saturn==82):
        print('Відповідь вірна') 
        _bal=_bal+3
    elif(saturn==4 or saturn==102 or saturn==46):
        print('Відповідь не вірна')
    else:
        print('Я вас не розумію')
    print('Скільки карликових планет в сонячній системі?')
    print('1  17  9  5')
    smallplenet=int(input())
    if(smallplenet==5):
        print('Відповідь вірна') 
        _bal=_bal+2
    elif(smallplenet==17 or smallplenet==9 or smallplenet==1):
        print('Відповідь не вірна')
    else:
        print('Я вас не розумію')
    print('Скільки планет сонячної системи мають кільця?')
    print('1  6  4  3')
    rings=int(input())
    if(rings==4):
        print('Відповідь вірна') 
        _bal=_bal+2
    elif(rings==3 or rings==6 or rings==1):
        print('Відповідь не вірна')
    else:
        print('Я вас не розумію')
    print('Скільки кілець має Уран?')
    print('13  18  100  78')
    uran=int(input())
    if(uran==13):
        print('Відповідь вірна') 
        _bal=_bal+3
    elif(uran==14 or uran<=14 ):
        print('Відповідь не вірна')
    else:
        print('Я вас не розумію')
    print('Ваш результат '+ str(_bal) + ' балів')

cosmos()