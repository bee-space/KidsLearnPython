#!/usr/bin/python3 

def cosmos():

    print('Бажаєте пройти наш тест?')    

    print('Напишіть так, або ні')                            
    cosmos={8,9, 82,5, 4, 13}
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
    cosmos=int(input())
    if(cosmos==8):
        print('Відповідь вірна')
        _bal=_bal+1
    elif(cosmos==9):
        print('Якщо враховувати плутон тоді так, але плутон вже не рахуєтся як планета')
        _bal=_bal+1
    elif(cosmos==1 or cosmos==4):
        print('Віповідь не вірна')
    else:
        print('Я вас не розумію')
    print('Скільки супутників має сатурн?')
    print('4   82   102   46')
    cosmos=int(input())
    if(cosmos==82):
        print('Відповідь вірна') 
        _bal=_bal+3
    elif(cosmos==4 or cosmos==102 or cosmos==46):
        print('Відповідь не вірна')
    else:
        print('Я вас не розумію')
    print('Скільки карликових планет в сонячній системі?')
    print('1  17  9  5')
    cosmos=int(input())
    if(cosmos==5):
        print('Відповідь вірна') 
        _bal=_bal+2
    elif(cosmos==17 or cosmos==9 or cosmos==1):
        print('Відповідь не вірна')
    else:
        print('Я вас не розумію')
    print('Скільки планет сонячної системи мають кільця?')
    print('1  6  4  3')
    cosmos=int(input())
    if(cosmos==4):
        print('Відповідь вірна') 
        _bal=_bal+2
    elif(cosmos==3 or cosmos==6 or cosmos==1):
        print('Відповідь не вірна')
    else:
        print('Я вас не розумію')
    print('Скільки кілець має Уран?')
    print('13  18  100  78')
    cosmos=int(input())
    if(cosmos==13):
        print('Відповідь вірна') 
        _bal=_bal+3
    elif(cosmos==14 or cosmos<=14 ):
        print('Відповідь не вірна')
    else:
        print('Я вас не розумію')
    print('Ваш результат '+ str(_bal) + ' балів')

cosmos()