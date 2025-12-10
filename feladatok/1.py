'''
1. Feladat
Írj egy programot, amely a felhasználótól bekéri egy kutya nevét, életkorát, fajtáját,
és azt hogy rendelkezik-e érvényes oltással veszettség ellen!
Az adatokat tárolja a program szótárban, és írja ki a képernyőre az adatszerkezetet!
'''

print('Adja meg a kutyája adatait?')
kutynev = input('Mi a kutyája neve?')
kutyeletkor = input('Hány éves a kutyája?')
kutyfajta = input('Milyen fajtájú a kutyája?')
oltas = input('Van a kutyának érvényes oltásal veszettség ellen? igen/nem')

kutyainfo = {}
kutyainfo['kutyaneve'] = kutynev
kutyainfo['kutya eletkora'] = kutyeletkor
kutyainfo['kutya fajtája'] = kutyfajta
kutyainfo['kutya veszettségi oltasa'] = oltas

for kulcs, ertek in kutyainfo:
    print(f'{kulcs} : {ertek}')