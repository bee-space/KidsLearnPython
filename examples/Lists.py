
print ('------------------')
print("HELLO LISTS")
print ('------------------')

#оголошення списку
list = [1,2,3,4,5]
print(list)

#оголошення списку тварин
animals = ['DoG', 'cat', 'snake', 'bird']
print(animals)
#додавання до списку нового елементу
animals.append('elephant')

#доступ до елементів списку через індекс, починаючи з нуля
print(animals[0])
print(animals[1])
print(animals[2])
print(animals[3])

#оголошення іншого списку тварин
myAnimals = ['monkey', 'perot']
print(myAnimals)

#вставка елемента в список
myAnimals.insert(1, 'dog')
print(myAnimals)

myAnimals.append('dog')

#розшрирення одного списку іншим
animals.extend(myAnimals)

#очищення списку
myAnimals.clear()

print(animals)
print(myAnimals)

print ('------------------')