import numpy as np
import re
import random

print("~~~~~~~~~~_NUEVA_PARTIDA_~~~~~~~~~~~~~~~_NUEVA_PARTIDA_~~~~~~~~~~~~~~~~~_NUEVA_PARTIDA_~~~~~~~~~\n" \
      "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

from utils import (player)
yo = player()
algoritmo = player()

counter=0
while np.any(yo.tablero == "■") and np.any(algoritmo.tablero == "■") :

    counter +=1

    print( f"\n\n                                <<<<<<|| RONDA #{counter} ||>>>>>>\n" )
    print(">>> TU disparas >>>")
    yo.disparar(algoritmo, rand=False)
    print("~~~~~~~~~~~~~~~~______TU tablero______~~~~~~~~~~~~~~~~~_____tablero del ENEMIGO_____~~~~~~~~~~~~~")
    for f1,f2 in zip(yo.tablero, algoritmo.vista_tablero):
        print("        ", f1, "               ", f2)
    
    algoritmo.disparar(yo, rand=True)
    print("~~~~~~~~~~~~~~~~______TU tablero______~~~~~~~~~~~~~~~~~_____tablero del ENEMIGO_____~~~~~~~~~~~~~")
    for f1,f2 in zip(yo.tablero, algoritmo.vista_tablero):
        print("        ", f1, "               ", f2)
    print("---^^^^^^---mira el disparo del ENEMIGO---^^^^^^-------------------------------------------------")


print( f"\n\n                                       <<<<<<|| FIN DEL JUEGO ||>>>>>>\n\n" )

if np.any(yo.tablero == "■"):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~¡ Has ganado TU !~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
elif np.any(algoritmo.tablero == "■"):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~¡ Ha ganado mi ALGORITMO !~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
else:
    print("¡ Empate !")
