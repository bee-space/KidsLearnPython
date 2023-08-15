print ('------------------')
print("HELLO TUPLE")
print ('------------------')

#Кортеж

#Кортежі використовуються для зберігання кількох елементів в одній змінній.
#Кортеж — це впорядкована та незмінна колекція.
#Кортежі записуються в круглих дужках.

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Щоб визначити, скільки елементів містить кортеж, скористайтеся функцією len():
print(len(thistuple))


tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# 'рядок' "рядок"
# 34 - int
# 34.0 - float
# true\false - bool 

#Кортеж із рядками, цілими числами та логічними значеннями:
tuple1 = ("abc", 34, True, 40, "male")

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

