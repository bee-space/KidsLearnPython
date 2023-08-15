#!/usr/bin/python3 

friends = ['Влад', 'Саша', 'Максим', 'Рома', 'Андрій', 'Юра', 'Артем', 'Вова', 'Міша']

def PrintWhileFriends():
    inx = 0
    while(inx < len(friends)):
        print(friends[inx])
        inx += 1

def PrintForFriends():
    for name in friends:
        print(name)

def CountFriends():
        #print('Кількість друзів: ' + str(len(friends)) )
        print('Кількість друзів:', len(friends))
#----------------------------------------

CountFriends()
PrintForFriends()
