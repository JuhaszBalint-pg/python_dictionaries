'''
3.1 Feladat
Írj egy programot, amely szótárban tárol adatokat (legalább egy int, str, és bool típusút).
A program a írja ki a képernyőre az adatszerkezet!
A felhasználónak legyen lehetősége ezt az adatszerkezetet egy kulcs-érték párral bővítenie.
A program végül írja ki a képernyőre a frissített adatszerkezetet!
'''

kedvencjatek = {
    'neve' : 'CS2',
    'órák játszva' : 1000,
    'telepítve?' : True,
}

for kulcs, ertek in kedvencjatek.items():
    print(f'{kulcs} : {ertek}')

print('Bővítsd az adatszerkezetet!')
adatszerkezetneve = input('Add meg az adat nevét!\n')
kedvencjatek[f'{adatszerkezetneve}'] = input('Add meg az adatszerkezet értékét!\n')

for kulcs, ertek in kedvencjatek.items():
    print(f'{kulcs} : {ertek}')