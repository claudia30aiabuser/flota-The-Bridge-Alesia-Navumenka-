import numpy as np
from utils import (crear_tablero)
                #    colocar_10_barcos_rand, 
                #             disparar_rand)


mitablero = crear_tablero(size=20)
vista_mitablero= crear_tablero(vista=True)


mi_flota=list(input("Indique los barcos con los cuales se juega esta partida, separando sus esloras por comas (max eslora es 4).\n" \
                    "Ejemplo (la flota clasica):\n 4, 3, 3, 2, 2, 2, 1, 1, 1, 1 [enter]\n" \
                    "Para usar la flota clasica pulse 0 [enter]."))
print(mi_flota)


disparos_anteriores = {"agua":set(), "tocado":[]}  # y tambien celdas alrededor de barcos hundidos
flota={"barco4":[], "barco3":[], "barco2":[], "barco1":[]}

print(mitablero)
print("===================================================")
print(vista_mitablero)




