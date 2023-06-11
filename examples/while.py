#!/usr/bin/python3 
print('придумайте пароль')

userpass=input()

print('Доступ до сховища даних')
print('Уведіть пароль у вас 3 спроби')

cnt_wron_pass=0

while(input()!=userpass):
    cnt_wron_pass=cnt_wron_pass+1
    if(cnt_wron_pass>2):
        print('Спроби закінчились')
        break
    print('пароль не вірний повторіть спробу')
else:
    print('пароль вірний. доступ надано')
print('програма завершена')