'''
3.2 Feladat
Módosítsd úgy a programot, hogy a felhasználónak többször is legyen lehetősége bővíteni az adatszerkezetet
'''

kedvencjatek = {
    'neve' : 'CS2',
    'órák játszva' : 1000,
    'telepítve?' : True,
}

for kulcs, ertek in kedvencjatek.items():
    print(f'{kulcs} : {ertek}')

#függvény helye
def errors(x):
    # try:
    #     if '.' in x:
    #         result = float(x)
    #         return result
    #     else:
    #         result = int(x)
    #         return result
    # except ValueError as e:
    #     if  x == 'True' or x == 'true' or x == 'igaz' or x == 'Igaz':
    #          result = True
    #          return result
    #     elif x == 'False' or x == 'false' or x == 'Hamis' or x == 'hamis':
    #          result = False
    #          return result



    
    try:
        if x.isnumeric():
            return int(x)
        elif x.count('.') > 0 and x.count('.') < 0:
            return float(x)
        elif x == 'True' or x == 'true' or x == 'igaz' or x == 'Igaz':
             return True
        elif x == 'False' or x == 'false' or x == 'Hamis' or x == 'hamis':
            return  False
        else:
            return str(x)
    except ValueError as e:
        print(f'{e}, a program value errorba futott.')
        
cycle = input('szeretnéd bővíteni az adatszerkezetet? (i/n)')
if cycle == 'i':
    fut = True
    while fut:
        adatkulcsneve = input('Add meg az adat nevét!\n')
        adat_ertek = input('Add meg az adatszerkezet értékét!\n')
        print(type(errors(adat_ertek)))
        question = input('Szeretnél további adatokat hozzáadni? (i/n)')
        if question == 'i':
            continue
        elif question == 'n':
            fut = False
elif cycle == 'n':
    exit()

for kulcs, ertek in kedvencjatek.items():
    print(f'{kulcs} : {ertek}')