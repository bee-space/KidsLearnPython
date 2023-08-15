
# Міша -   14
# Саша -   13
# Віра -   4
# Андрій - 7

# Міша -   2008
# Саша -   2009
# Віра -   2019
# Андрій - 2016

# Міша -   misha@gmail.com
# Саша -   sasha@gmail.com
# Віра -   visha@gmail.com
# Андрій - andrii@gmail.com

list = {'Misha', 'Sasha', 'Vira', 'Andrii'}
dict_years = {'Misha':2008, 'Sasha':2009, 'Vira':2019, 'Andrii':2016}
print(dict_years['Misha'])
print(dict_years['Vira'])
dict_emails = {'Misha':'misha@gmail.com', 'Sasha':'sasha@gmail.com', 'Vira':'visha@gmail.com', 'Andrii':'andrii@gmail.com'}

print('емейл Саши ' + dict_emails['Sasha'])
print('рік народження Саши {}'.format(dict_years['Sasha']))

# скопонуємо все в окремий метод, який з усіх словників витягне інформацію за ключем
# в даному випадку ключем є імя людини
# приклад примітивної бази даних.
def GetInfo(name):
    result = "info about " + name + ": "
    result += "email:" + dict_emails[name] + " "
    result += "year:" + str(dict_years[name]) + " "
    return result

print(GetInfo('Vira'))
