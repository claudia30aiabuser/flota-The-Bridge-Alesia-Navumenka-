import numpy as np
import re
from utils import (player)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" \
      "~~~~~~~~~~_NUEVA_PARTIDA_~~~~~~~~~~~~~~~_NUEVA_PARTIDA_~~~~~~~~~~~~~~~~~_NUEVA_PARTIDA_~~~~~~~~~\n" \
      "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
yo = player()
maquina = player()

# size = int(input("EL TAMANO DEL TABLERO? \n filas x columnas, filas=columnas="))
# mi_flota=list(input("Indique los barcos con los cuales se juega esta partida, separando sus esloras por comas (max eslora es 4).\n" \
#                     "Ejemplo (la flota clasica):  4, 3, 3, 2, 2, 2, 1, 1, 1, 1 \n" \
#                     "Para usar la flota clasica pulse 0 [enter].\n"))


print(yo.tablero, "            ", yo.vista_tablero)
print("mi flota = ", yo.flota)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("flota de maquina = ", maquina.flota)
print(maquina.tablero, "            ", maquina.vista_tablero)



counter=0
while np.any(yo.tablero == "■") or np.any(maquina.tablero == "■"):
    counter +=1
    print( f"****************__MI turno__#{counter}__******************" )
    yo.disparar(rand=False)
    print(yo.tablero, "            ", maquina.vista_tablero)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    print( f"************__turno de MAQUINA__#{counter}__******************" )
    maquina.disparar(rand=True)
    print(yo.tablero, "            ", maquina.vista_tablero)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~_________________~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n \
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~__FIN del juego__~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" )

if np.any(yo.tablero == "■"):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~¡ Has ganado TU !~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
elif np.any(maquina.tablero == "■"):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~¡ Ha ganado MAQUINA !~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
else:
    print("¡ Empate !")
