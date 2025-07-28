import os, time
clean = 'clear'
'''
Quiero un menu que tenga las siguientes opciones:
    1) Un sistema para renombrar los meses del 1 al 13.
    2) Un sistema para ver un mes en concreto con su 
       respectivo dia correspondiente al año actual.
    3) Un calculo que determine tu nuevo cumpleaños segun tu dia mes y año.
    4) Salir.
'''
calendario = {
    'm1': ['1'],
    'm2': ['2'],
    'm3': ['3'],
    'm4': ['4'],
    'm5': ['5'],
    'm6': ['6'],
    'm7': ['7'],
    'm8': ['8'],
    'm9': ['9'],
    'm10': ['10'],
    'm11': ['11'],
    'm12': ['12'],
    'm13': ['13'],
    'DAN': ['0']
}

def string_normalizer(word: str):

    word = word.strip()

    while '  ' in word:
        word = word.replace('  ','')

    word = word.title()

    return word

def naming():
    for i in calendario:
        os.system(clean)
        while True:
            match = False
            nombre = string_normalizer(input(f'Ingresa el nuevo nombre del mes nro {calendario[i][0]}'))
            for j in calendario:
                for k in calendario[j]:
                    if nombre == k:
                        match = True
                        break
            if not match:
                calendario[i].append(nombre)
                break
            else:
                print('Dos meses no pueden llevar el mismo nombre >=[')
    
    return()

def mes():
    return

def cumple():
    return