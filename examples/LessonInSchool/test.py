
name = input("Введіть своє ім'я: ")
answer = input('Привіт, '+ name + ', в мене є декілька загадок для тебе, почнемо?(Так/Ні)\n')

if answer == 'Так' or answer == 'так':
    balls = 0
    answer = input('                Питання 1\nЧерез воду він проводить, а сам з місця вік не сходить.\nВідповідь: ')
    if answer == 'Міст' or  answer ==  'міст':
        balls = balls + 1
        print('Непогано для початку, йдемо далі!')
    else:
        print('Нажаль, це неправильна відповідь.')
    
    answer = input('                Питання 2\nХоч не літак, а крилатий, без крил не може працювати.\nВідповідь: ')
    if answer == 'Вітряк' or answer ==  'вітряк':
        balls = balls + 1
        print('Правильно')
    else:
        print('Не вгадав.')

    answer = input('                Питання 3\nМов маленький м’ячик, висить, а не скаче, рум’яне, гладеньке, на смак солоденьке.\nВідповідь: ')
    if answer == 'Яблуко' or answer ==  'яблуко':
        balls = balls + 1
        print('Добре')
    else:
        print('Невірно')

    answer = input('                Питання 4\nДерев’яний та довгенький, маю носик я гостренький. На білому слід лишаю, усіх діток потішаю.\nВідповідь: ')
    if answer == 'Олівець' or  answer ==  'олівець':
        balls = balls + 1
        print('Правильно, молодець!!')
    else:
        print('Не правильно')

    answer = input('                Питання 5\nКоли хочеш ти читати, то повинен мене знати, a коли мене не знаєш, то нічого не вчитаєш.\nВідповідь: ')
    if answer == 'Абетка' or  answer ==  'абетка':
        balls = balls + 1
        print('Вірно.')
    else:
        print('Не вгадав.')
    
    answer = input('                Питання 6\nСпритний майстер у стрибках: На деревах, по гілках. Вся руда, пухнастий хвіст, рідний дім для неї – ліс.\nВідповідь: ')
    if answer == 'Білка' or  answer == 'білка':
        balls = balls + 1
        print('Молодець!')
    else:
        print('Ні.')
    
    answer = input('                Питання 7\nЗ небокраю, з-за діброви, вийшли воли чорноброві, принесли водиці дзбан, полили і ліс, і лан.\nВідповідь: ')
    if answer == 'Хмари' or  answer ==  'хмари':
        balls = balls + 1
        print('Правильно.')
    else:
        print('Не правильно.')

    answer = input('                Питання 8\nУночі гуляє, а вдень спочиває, має круглі очі, бачить серед ночі\nВідповідь: ')
    if answer == 'Сова' or  answer ==  'сова':
        balls = balls + 1
        print('Вірно!')
    else:
        print('Не правильно!')

    answer = input('                Питання 9\nВін скрізь: у полі і в саду, а3 в дім не попаде, і я тоді лиш з дому йду, коли вже він не йде.\nВідповідь: ')
    if answer == 'Дощ' or  answer == 'дощ':
        balls = balls + 1
        print('Вгадав, молодець!')
    else:
        print('Не вгадав.')

    answer = input('                Питання 10\nНеначе паровоз, гуде, шумить, кипить, і пара йде, смачний заварює нам чай. Хто ж він такий? От відгадай\nВідповідь: ')
    if answer == 'Чайник' or  answer ==  'чайник':
        balls = balls + 1
        print('Добре.')
    else:
        print('Не правильно.')

    answer = input('                Питання 11\nХто завжди правду каже? Який є, таким покаже, і без слів про все рас скаже. На нього дивишся, а себе бачиш.\nВідповідь: ')
    if answer == 'Дзеркало' or  answer ==  'дзеркало':
        balls = balls + 1
        print('Правильно!')
    else:
        print('Невірно.')

    answer = input('                Питання 12\nЯ порою дощовою – наче дах над головою. При собі мене тримають, а як дощ пройде – складають.\nВідповідь: ')
    if answer == 'Парасолька' or  answer ==  'парасолька':
        balls = balls + 1
        print('Правильно!')
    else:
        print('Невірно.')
    
    if balls <= 6 and balls > 0:
        print(name + ', ти отримав', balls ,'балів\nНаступний раз повезе більше')
    elif balls == 0:
        print(name + ', нажаль,ти не дав жодної правильної відповіді')
    elif balls == 12:
        print('УРА! Вітаю! Чудовий результат! 12 балів')
    else:
        print(name + ', ти отримав', balls ,'балів')

    print(name + ' дякую за участь')
    
elif answer != 'ні':
    print('Відповідати треба так або ні')

else:
    print("Окей, до нових зустрічів!")  
