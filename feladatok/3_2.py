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
cycle = input('szeretnéd bővíteni az adatszerkezetet? (i/n)')
if cycle == 'i':
    fut = True
    while fut:
        adatkulcsneve = input('Add meg az adat nevét!\n')
        kedvencjatek[adatkulcsneve] = input('Add meg az adatszerkezet értékét!\n')
        #value error, függvény hívása
        question = input('Szeretnél további adatokat hozzáadni? (i/n)')
        if question == 'i':
            continue
        elif question == 'n':
            fut = False
elif cycle == 'n':
    exit()

for kulcs, ertek in kedvencjatek.items():
    print(f'{kulcs} : {ertek}')