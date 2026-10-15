import numpy as np
import re
from utils import (player)

print("~~~~~~~~~~_NUEVA_PARTIDA_~~~~~~~~~~~~~~~_NUEVA_PARTIDA_~~~~~~~~~~~~~~~~~_NUEVA_PARTIDA_~~~~~~~~~\n" \
      "~~~~~~~~~~~~~~~~______TU tablero______~~~~~~~~~~~~~~~~~_____tablero del ENEMIGO_____~~~~~~~~~~~~~")
yo = player()
maquina = player()


for f1, f2 in zip(yo.tablero, yo.vista_tablero):
    print("            ", f1, "            ", f2)

print("mi flota = ", yo.flota)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("flota de maquina = ", maquina.flota)
for f1,f2 in zip(maquina.tablero, maquina.vista_tablero):
    print("            ", f1, "               ", f2)



counter=0
while np.any(yo.tablero == "■") and np.any(maquina.tablero == "■"):
    counter +=1

    print( f"\n\n                                   || RONDA #{counter} ||\n\n" )
    print("~~~~~~~~~~~~~~~~______TU tablero______~~~~~~~~~~~~~~~~~_____tablero del ENEMIGO_____~~~~~~~~~~~~~")
    yo.disparar(maquina, rand=False)
    for f1,f2 in zip(yo.tablero, maquina.vista_tablero):
        print("            ", f1, "               ", f2)


    print("~~~~~~~~~~~~~~~~______TU tablero______~~~~~~~~~~~~~~~~~_____tablero del ENEMIGO_____~~~~~~~~~~~~~")
    maquina.disparar(yo, rand=True)
    for f1,f2 in zip(yo.tablero, maquina.vista_tablero):
        print("            ", f1, "               ", f2)


print( f"\n\n                                   || FIN DEL JUEGO ||\n\n" )

if np.any(yo.tablero == "■"):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~¡ Has ganado TU !~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
elif np.any(maquina.tablero == "■"):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~¡ Ha ganado MAQUINA !~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
else:
    print("¡ Empate !")
