
print ('------------------')
print("HELLO LIST")
print ('------------------')

#СПИСОК

#Списки використовуються для збереження кількох елементів в одній змінній.
#Списки створюються за допомогою квадратних скобок:

#оголошення списку чисел
list = [1,2,3,4,5]
print(list)

#оголошення списку тварин
animals = ['dog', 'cat', 'snake', 'bird']
print(animals)

#Елементи списку впорядковані, змінні та допускають дублювання значень.
#Елементи списку проіндексовано, перший елемент має індекс [0], другий елемент має індекс [1] тощо.

#в списку дозволені дублікати 
animals = ['dog', 'cat', 'snake', 'bird', 'dog', 'cat']
print(animals)

# Якщо ти додаєш елемент в список, то він додається в кінці списку
#додавання до списку нового елементу
animals.append('elephant')

# ДОВЖИНА СПИСКУ
# Щоб визначити кількість елементів у списку, скористайтеся функцією len(): 
print(len(animals))


# Елементи списку - Типи даних
# Елементи списку можуть мати будь-який тип даних:
list1 = ["apple", "banana", "cherry"] # тип рядок
list2 = [1, 5, 7, 9, 3]               # ціле число
list3 = [True, False, False]          # булеве значення

#Список може містити різні типи даних:
list1 = ["abc", 34, True, 40, "male"]

# З точки зору Python, списки визначаються як об’єкти з типом даних "list" ("список"):

print("З точки зору Python, списки визначаються як об’єкти з типом даних \"list\" (\"список\"):")
print(type(animals))


#доступ до елементів списку через індекс, починаючи з нуля
print(animals[0]) # 1-й елемента
print(animals[1]) # 2-й елемента
print(animals[2]) # 3-й елемента
print(animals[3]) # 4-й елемента

# Негативне індексування!
# Цікавий момент! ідексувати можна негативно.
# тоді -1 - це останні елемент списку, -2 - це передостанній
print(animals[-1])
print(animals[-2])


#Діапазон індексів
#Ти можеш вказати діапазон індексів, вказавши, де починати та де закінчувати діапазон.

print(animals[2:5])
#Примітка: Пошук почнеться з індексу 2 (включно) і завершиться з індексу 5 (не включено).

#Якщо пропустити початкове значення, діапазон розпочнеться з першого елемента:
print(animals[:5])
#Якщо пропустити кінцеве значення, діапазон розпочнеться з вказаного елемента і закінчиться останнім
print(animals[2:])


#Перевірте, чи існує елемент
#Щоб визначити, чи присутній певний елемент у списку, використовуйте ключове слово in:
fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
  print("Так, 'apple' є в списку фруктів")

# додавання елементу в список
fruits.append('mango')
print(fruits)

# змінити значення певного елемента, звертаємось до індексу
fruits[1] = 'cherry'
print(fruits)

#вставка елемента в список
fruits.insert(1, 'blackberry') # вставляємо елемент в другий елемент списку (памятай, що індексування починається з нуля)
print(fruits)
fruits.insert(3, 'blackberry') # вставляємо елемент в четвертий елемент списку (памятай, що індексування починається з нуля)
print(fruits)


# розшрирення одного списку іншим
# Щоб додати елементи з іншого списку до поточного списку, використовуй метод extend().
animals.extend(fruits)
print(animals)

# ВИДАЛЕННЯ ЕЛЕМЕНТІВ ЗІ СПИСКУ

# Видаємо конткретний елемент зі списку.
# в метод remove() передає параметром елемент списку
fruits.remove("blackberry")
print(fruits)

# видалити визначений за індексом елемент зі списку.
# користуйся методом pop()
fruits.pop(1) # видаляємо другий елемент:

#ящо в метод pop() не передавати індекс елемента на видалення, то метод видалит останній елемент

# очищення списку
# метод clear() очищає список. Метод вхідних параметрів не має
fruits.clear()

#Перебрати список

# перебрати елементи списку за допомогою циклу for:
for x in fruits:
  print(x)
# перебрати елементи списку за допомогою циклу while:
i = 0
while i < len(fruits):
  print(fruits[i])
  i = i + 1

# сортування списку 
# для сортування використовуй метод sotr()
fruits.sort()
print(fruits)

# для сортування у зворотньому порядку використовуй метод sotr(),але передай параметр сортування reverse = true
#fruits.sort(reverse = True)
#або
#fruits.sort(True)
print(fruits);

#Методи списку 
# append()	Додає елемент в кінець списку
# clear()	Видаляє всі елементи зі списку
# copy()	Поверне скопійований список
# count()	Поверне число елементів з визначеним значенням
# extend()	Додає елементи списку (або будь-які ітеровані), в кінець поточного списку
# index()	Поверне індекс першого елемента з визначеним значенням
# insert()	Додає елемент у визначену позицію
# pop()	    Видаляє елемент на визначеній позиції
# remove()	Видаляє елемент з визначеним значенням
# reverse()	Обертає порядок списку
# sort()	Сортує список

# Вправи:
# 1. Надрукуйте другий елемент в списку fruits.
# 2. Change the value from "apple" to "kiwi", in the fruits list.
# 3. Use the append method to add "orange" to the fruits list.
# 4. Use the insert method to add "lemon" as the second item in the fruits list.
# 5. Use the remove method to remove "banana" from the fruits list.
# 6. Use negative indexing to print the last item in the list.
# 7. Use a range of indexes to print the third, fourth, and fifth item in the list.
# 8. Use the correct syntax to print the number of items in the list.

print('################')

fruits = ['apple', 'banana', 'cherry', 'mango', 'pear']
# 1
print(fruits[1])

# 2
fruits[0] = 'kiwi'

# 3
fruits.append('orange')

# 4
fruits.insert(1,'lemon')
print(fruits)

# 5
fruits.remove('banana')
print("#5")
print(fruits)

#6
print(fruits[-1])

#7 
print("#7")
print(fruits)
print(fruits[2:5])

#8
print('count items: {0}'.format(len(fruits)))

print ()
print ('# ' * 10 + ' Python is cool ' + '# ' * 10)