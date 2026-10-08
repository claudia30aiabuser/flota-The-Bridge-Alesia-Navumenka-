import numpy as np
from flota_funciones import (colocar_10_barcos_rand, 
                            disparar)



tablero=np.full((12, 12), ".")
tablero[0, :]=np.arange(12)
tablero[:, 0]=np.arange(12)
tablero[11, :]=np.full((1,12), "|")
tablero[:, 11]=np.full((1,12), "|")

vista_del_tablero = np.full((10, 10), ".")
vista_del_tablero = np.pad(vista_del_tablero, 1, constant_values="|")
vista_del_tablero[0, :11]=np.arange(11)
vista_del_tablero[:11, 0]=np.arange(11)


disparos_anteriores = set()

colocar_10_barcos_rand(tablero)


# bordes de tablero bonitos
# tablero[0, :]=np.arange(12)
# tablero[:, 0]=np.arange(12)
# tablero[11, :]=np.full((1,12), "|")
# tablero[:, 11]=np.full((1,12), "|")



print("==================NUEVA=PARTIDA==================NUEVA=PARTIDA===================NUEVA=PARTIDA==\n" \
      "==NUEVA=PARTIDA==================NUEVA=PARTIDA===================NUEVA=PARTIDA==================\n" \
      "==================NUEVA=PARTIDA==================NUEVA=PARTIDA===================NUEVA=PARTIDA==")
print(tablero)    
print("Como se ve mi tablero:")
print(vista_del_tablero)



disparar(tablero, vista_del_tablero, disparos_anteriores)
print(tablero)
print("set de disparos anteriores: ", disparos_anteriores)    
print(vista_del_tablero)


disparar(tablero, vista_del_tablero, disparos_anteriores)
print(tablero)
print("set de disparos anteriores: ", disparos_anteriores)    
print(vista_del_tablero)


disparar(tablero, vista_del_tablero, disparos_anteriores)
print(tablero)
print("set de disparos anteriores: ", disparos_anteriores)    
print(vista_del_tablero)


disparar(tablero, vista_del_tablero, disparos_anteriores)
print(tablero)
print("set de disparos anteriores: ", disparos_anteriores)    
print(vista_del_tablero)


disparar(tablero, vista_del_tablero, disparos_anteriores)
print(tablero)
print("set de disparos anteriores: ", disparos_anteriores)    
print(vista_del_tablero)
