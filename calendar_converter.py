'''
Quiero un menu que tenga las siguientes opciones:
    1) Un sistema para renombrar los meses del 1 al 13.
    2) Un sistema para ver un mes en concreto con su 
       respectivo dia correspondiente al año actual.
    3) Un calculo que determine tu nuevo cumpleaños segun tu dia mes y año.
    4) Salir.
'''

import os, time, func_calendar as fn 

menu = """
+---------MENU-CALENDAR---------+
| 1) Renombrar los meses.       |
| 2) Ver Mes Calendario.        |
| 3) Calcular nuevo cumpleaños. |
| 4) Salir del sistema.         |
+-------------------------------+
"""
clean = 'clear'                                 #Comando de limpiar pantalla en unix
#clean = 'cls'                                  #Comando de limpiar pantalla en windows

while True:
    os.system(clean)
    print(menu)
    page = input('- ')

    if page == '1':
        pass
    if page == '2':
        pass
    if page == '3':
        pass
    if page == '4':
        print('Saliendo . . .')
        break
    else:
        print('Error. Opción invalida.')
