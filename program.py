import writers

print('Бібліотека')

writers.GetAllWriters()
print('Введіть письменика')
writer=input()
writers.GetBirthday(writer)
writers.GetPlaceOfBirth(writer)