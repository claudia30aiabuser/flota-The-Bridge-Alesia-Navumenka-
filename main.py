import numpy as np
from utils import (crear_tablero,
                   colocar_barcos_rand, 
                   colocar_barcos,
                   disparar_rand,
                   flota, disparos_anteriores)


mitablero = crear_tablero(size=5)
vista_mitablero= crear_tablero(size=5, vista=True)
mtab = crear_tablero(size=5)
mtab_view = crear_tablero(size=5, vista=True)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" \
      "~~~~~~~~~~_NUEVA_PARTIDA_~~~~~~~~~~~~~~~_NUEVA_PARTIDA_~~~~~~~~~~~~~~~~~_NUEVA_PARTIDA_~~~~~~~~~\n" \
      "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
mi_flota=list(input("Indique los barcos con los cuales se juega esta partida, separando sus esloras por comas (max eslora es 4).\n" \
                    "Ejemplo (la flota clasica):  4, 3, 3, 2, 2, 2, 1, 1, 1, 1 \n" \
                    "Para usar la flota clasica pulse 0 [enter].\n"))

colocar_barcos(mitablero, mi_flota)
print(mitablero)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(vista_mitablero)
print("mi_flota=", mi_flota)
print("flota=", flota)
print("===================================================")
colocar_barcos(mtab, mi_flota)
print(mtab)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(mtab_view)

counter=0
while np.any(mitablero == "■") or np.any(mtab == "■"):
    counter +=1
    print( f"****************__MI turno__#{counter}__******************" )
    disparar_rand(mtab, mtab_view)
    print(mtab)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(mtab_view)

    print(f"+++++++++++++___Turno de MAQUINA___#{counter}__+++++++++++++")
    disparar_rand(mitablero, vista_mitablero)
    print(mitablero)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(vista_mitablero)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" \
      "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~__FIN de juego__~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" \
      "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

if np.any(mitablero == "■"):
    print("¡ He ganado yo !")
elif np.any(mtab == "■"):
    print("¡ Ha ganado MAQUINA !")
else:
    print("¡ Empate !")
