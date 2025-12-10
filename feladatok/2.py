'''
2. Feladat
Írj egy programot, amely szótárban tárolja egy macska nevét, korát.
A felhasználónak legyen lehetősége megváltoztatni az egyik tárolt adatot.
A program írja ki a felhasználó választása alapján az egyik adatot, kérdezze meg,
mire módosítsa, végül írja ki a képernyőre a frissített adatszerkezetet!
'''

macskainfo = {}
print('Adja meg a macska adatait?')
macskainfo['Név:'] = input('Adja meg a macskája nevét!')
macskainfo['Életkor:'] = input('Adja meg a macskája életkorát!')

for kulcs, ertek in macskainfo.items():
    print(f'{kulcs} : {ertek}')

változtatás = input('Szeretne változtatni az adatokon? (Igen/Nem)\n')
if változtatás == 'Igen':
    melyiket = input('Melyiket szeretné változtatni? (Név/Életkor)')
    if melyiket == 'Név':
        macskainfo['Név:'] = input('Adja meg a macskája helyes nevét!')
        for kulcs, ertek in macskainfo.items():
            print(f'{kulcs} : {ertek}')
    else:
        macskainfo['Életkor:'] = input('Adja meg a macskája helyes életkorát!')
        for kulcs, ertek in macskainfo.items():
            print(f'{kulcs} : {ertek}')
else:
    exit()

