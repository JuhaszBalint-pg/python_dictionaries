ures_szotar = {}

szemely_dict = {
    'nev': 'Kis Fernc',
    'kor': 25,
    'varos': 'Budapest',
    'telefon': '70/1346432'
}

print(szemely_dict['nev'])  # adat kiiratása kulcs alapján
print(szemely_dict['kor'])

print(szemely_dict.get('kor')) # más kiiratási módszer

print(szemely_dict.get('telefon', 'Nincs a szótárban ez a kulcs')) #ha jelen van a veszző utáni stringet nem írja ki

szemely_dict['kor'] = 26
print(szemely_dict.get('kor')) #adat módosítása

# kulcs-érték pár törlése
print(szemely_dict.get('varos'))
del szemely_dict['varos']
print(szemely_dict.get('varos', 'A város adata nincsen megadva'))

#kulcs-érték pár hozzáadása
szemely_dict['neme'] = 'férfi'
print(szemely_dict['neme'])

#.get néküli check, in operátor
if 'név' in szemely_dict:
    print('a keresett kulcs megtalálható a szótárban')

if 'bankszamla' not in szemely_dict:
    print('Nincsen a a tárban a keresett kulcs')

#az összes kulcs-érték pár elérése:
for kulcs, érték in szemely_dict.items():
    print(f'{kulcs}, {érték}')