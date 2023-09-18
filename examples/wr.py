
writers = {94:'Тарас Григорович Шевченко', 22:'Іван Якович Франко', 347:'Рильський Максим Тадейович', 4:'Всеволод Зінов́ійович Нестайко', 5:'Данієль Деффо'}
birthday={94:'25.02.1814', 2:'27.08.1856', 347:'24.07.1964', 4:'30.01.1930'}
cityvillage={94:'с.Моринці', 2:'с.Нагуєвичі', 347:'м.Київ', 4:'м.Бердичів'}
region={94:'Київська', 2:'Львівська', 347:'Київська', 4:' Житомирська'}


def GetAllWriters():
    idx=0
    for writer in writers:
        keys_list = list(writers.keys())
        values_list = list(writers.values())
        print('{0}.{1}'.format(keys_list[idx], values_list[idx]))
        idx+=1

def GetBirthday(writer):
    print (birthday[writer])
    
def GetPlaceOfBirth(writer):
    print('Письменик народився в {0} {1} обл.'.format(cityvillage[writer],region[writer]))

