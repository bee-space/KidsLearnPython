#!/usr/bin/python3 


def testAbrams():
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
        print('Назвіть основний бойовий танк Америки?')
        print('а)М1 Абрамс б)Леопард 2 А4 в)Челенджер 2 г)Т 90')
        America=input()
        if(America=='М1 Абрамс'):
                print('Відповідь вірна')
                _bal=_bal+1
        else:
                print('Відповідь не вірна')

        print('З якого року почалась серійне виробництво Абрамсів?')
        print('2000 1980 2010 1990')
        year=int(input())
        if(year==1980):
                print('Відповідь вірна') 
                _bal=_bal+2
        else:
                print('Відповідь не вірна')
        print('Зі скількох людей складаєтся екіпаж Абрамса?')
        print('2  3  4  5')
        team=int(input())
        if(team==4):
                print('Відповідь вірна') 
                _bal=_bal+1
        else:
                print('Відповідь не вірна')
        print('Який тип гармати встановлений на Абрамсі?')
        print('Глаткоствольна, Нарізна, Полігональна Нарізна')
        gun=input()
        if(gun=='Нарізна'):
                print('Відповідь вірна') 
                _bal=_bal+1
        elif(gun=='Глаткоствольна'):
                print('Починаючи з версії М1А1 встановлена Глаткоствольна гармата.')
                _bal=_bal+1
        else:
                print('Відповідь не вірна')
        print('Який калібр гармати Абрамса (мм)?')
        print('120  105  100  150')
        caliber=int(input())
        if(caliber==105):
                print('Відповідь вірна') 
                _bal=_bal+1
        elif(caliber==120):
                print('Починаючи з версії М1А1 встановлена 120 міліметрова гармата.')
                _bal=_bal+1
        else:
                print('Відповідь не вірна')
        print('Яка потужність двигуна Абрамс(к.с.)?')
        print('1500  1000  1100  2000')
        power=int(input())
        if(power==1500):
                print('Відповідь вірна') 
                _bal=_bal+2
        else:
                print('Відповідь не вірна')      
        print('Яка швидкість по шосе Абрамса (км/год?)')
        print('72 100 66 50')
        speed=int(input())
        if(speed==72):
                print('Відповідь вірна') 
                _bal=_bal+3
        elif(speed==66):
                print('Починаючи з версії М1А1 розвиває швидкість по шосе 66,8 км/год.')
                _bal=_bal+3
        else:
                print('Відповідь не вірна') 

        print('Ваш результат '+ str(_bal) + ' балів')

testAbrams()