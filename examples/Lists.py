
print ('------------------')
print("HELLO LISTS")
print ('------------------')

#оголошення списку
list = [1,2,3,4,5]
print(list)

#оголошення списку тварин
animals = ['dog', 'cat', 'snake', 'bird']
print(animals)
#додавання до списку нового елементу
animals.append('elephant')

#оголошення іншого списку тварин
myAnimals = ['monkey', 'perot']

print(animals)
print(myAnimals)
#розшрирення одного списку іншим
animals.extend(myAnimals)

#очищення списку
myAnimals.clear()

print(animals)
print(myAnimals)

print ('------------------')