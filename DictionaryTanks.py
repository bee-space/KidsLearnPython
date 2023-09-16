
tanks=['T-26','Panzer III','M2','Tetrarch','Char B1','Strv m/42']
tankcaliber={'T-26':'45-мм','Panzer III':'37-мм','M2':'37-мм','Tetrarch':'40-мм','Char B1':'75-мм, 47-мм','Strv m/41':'37-мм'}
tankSpeed={'T-26':'30 км/г','Panzer III':'35 км/г','M2':'43 км/г','Tetrarch':'64 км/г','Char B1':'28 км/г','Strv m/41':'43 км/г'}
tankCrew={'T-26':'3','Panzer III':'5','M2':'6','Tetrarch':'3','Char B1':'4','Strv m/42':'4',}
tankArmorСorps={'T-26':'15/15/15/10/6-мм','Panzer III':'30/9°,25/87°,30/21—52° — 25/75°/30/0°,20/30°,20/65°/20/10°,16','M2':'6','Tetrarch':'3','Char B1':'4','Strv m/42':'4',}
tankArmorTower={'T-26':'15/15/15/6-мм','Panzer III':'30/15°,30/25°,30/0—25°,10/83—90°','M2':'6','Tetrarch':'3','Char B1':'4','Strv m/42':'4',}
tankCountry={'T-26':'срср','Panzer III':'Німетчина','M2':'6','Tetrarch':'3','Char B1':'4','Strv m/42':'4',}
tankYearsProduction={'T-26':'1931–1941-р','Panzer III':'1937—1943-р','M2':'6','Tetrarch':'3','Char B1':'4','Strv m/42':'4',}
tankWeight={'T-26':'8-т','Panzer III':'19,5-т','M2':'6','Tetrarch':'3','Char B1':'4','Strv m/42':'4',}
tankClearance={'T-26':'380-мм','Panzer III':'385-мм','M2':'6','Tetrarch':'3','Char B1':'4','Strv m/42':'4',}
tankDimensions={
    'T-26':'4620/2445/2330-мм',
    'Panzer III':'5','M2':'6',
    'Tetrarch':'3','Char B1':'4',
    'Strv m/42':'4'
    }

print('Калібр танка Т-26 '+tankcaliber['T-26'])
print('Швидеість по шосе танка Strv m/41 '+tankSpeed['Strv m/41'])
print('Екіпаж танку Tetrarch '+tankCrew['Tetrarch'])



def GetTankSpeed(tank):
    return tankSpeed[tank]
    
def GetTankCrew(tank):
    return tankCrew[tank]
print(tanks)
print('Ведіть незву танка.')
tank=input()
speed=GetTankSpeed(tank)
print('Швидкість танку {0}. Екіпаж {1}'.format(speed, GetTankCrew(tank)))
print()









#Я не зробив базу данних про однокласників томущо я не знав в них стільки інформації.
#Але я зробив базу данних про танки.
#Це що я зробив це ще не все я хочу сюди ще багато чого добавити. 








