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

##CountFriends()
##PrintForFriends()

count = 3
say = 'Hello, I am ' + str(count) + '.' + ' How are you?'
print(say)

say2 = 'Hello, I am {0}. How are you?'
print(say2.format(count))

say3 = 'у машини {1} колеса, у мотоцикла {0} колеса, у самоката {2} колеса'
print(say3.format(4, 2, 2))