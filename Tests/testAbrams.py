#!/usr/bin/python3 


def testAbrams():
        print('Бажаєте пройти наш тест?')    
        print('Напишіть так, або ні')    
        #list                        
        true_answer_list = [1980, 'Нарізна', 105, 'Глаткоствольна',
                             'М1 Абрамс', 120, 1500, 72, 66, 4]
        
        user_answer = input()

        if(user_answer.lower() == 'так'):
                print('Добре, тоді продовжемо')
        elif(user_answer.lower() == 'ні'):
                 print('Добре, допобачення')
                 return
        else:
                print('Я вас не розумію')
                return
        _bal=0

        print('Назвіть основний бойовий танк США?')
        print('а)М1 Абрамс б)Леопард 2 А4 в)Челенджер 2 г)Т 90')
        
        user_answer = input()

        if(user_answer.lower() == true_answer_list[0].lower()):
                print('Відповідь вірна')
                _bal=_bal+1
        else:
                print('Відповідь не вірна')

        print('З якого року почалась серійне виробництво Абрамсів?')
        print('2000 1980 2010 1990')
        
        user_answer = int(input())

        if(user_answer == true_answer_list[1]):
                print('Відповідь вірна') 
                _bal=_bal+2
        else:
                print('Відповідь не вірна')

        print('Зі скількох людей складаєтся екіпаж Абрамса?')
        print('2  3  4  5')
        
        user_answer = int(input())
        if(user_answer == true_answer_list[3]):
                print('Відповідь вірна') 
                _bal=_bal+1
        else:
                print('Відповідь не вірна')
        print('Який тип гармати встановлений на Абрамсі?')
        print('Глаткоствольна, Нарізна, Полігональна Нарізна')
        
        user_answer = int(input())
        if(user_answer == true_answer_list[4]):
                print('Відповідь вірна') 
                _bal=_bal+1
        elif(user_answer == true_answer_list[5]):
                print('Починаючи з версії М1А1 встановлена Глаткоствольна гармата.')
                _bal=_bal+1
        else:
                print('Відповідь не вірна')

        print('Який калібр гармати Абрамса (мм)?')
        print('120  105  100  150')

        user_answer = int(input())
        if(user_answer == true_answer_list[6]):
                print('Відповідь вірна') 
                _bal=_bal+1
        elif(user_answer == true_answer_list[7]):
                print('Починаючи з версії М1А1 встановлена 120 міліметрова гармата.')
                _bal=_bal+1
        else:
                print('Відповідь не вірна')
        print('Яка потужність двигуна Абрамс(к.с.)?')
        print('1500  1000  1100  2000')
        
        user_answer = int(input())
        if(user_answer == true_answer_list[8]):
                print('Відповідь вірна') 
                _bal=_bal+2
        else:
                print('Відповідь не вірна')      
        
        print('Яка швидкість по шосе Абрамса (км/год?)')
        print('72 100 66 50')
        
        user_answer = int(input())
        if(user_answer == true_answer_list[9]):
                print('Відповідь вірна') 
                _bal=_bal+3
        elif(user_answer == true_answer_list[10]):
                print('Починаючи з версії М1А1 розвиває швидкість по шосе 66,8 км/год.')
                _bal=_bal+3
        else:
                print('Відповідь не вірна') 

        print('Ваш результат '+ str(_bal) + ' балів')

testAbrams()