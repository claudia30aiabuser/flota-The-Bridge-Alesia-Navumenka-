import numpy as np
from flota_funciones import (colocar_10_barcos_rand, 
                            disparar_rand)



tablero=np.full((12, 12), ".")
tablero[0, :]=np.arange(12)
tablero[:, 0]=np.arange(12)
tablero[11, :]=np.full((1,12), "|")
tablero[:, 11]=np.full((1,12), "|")

vista_del_tablero = np.full((12, 12), ".")
# vista_del_tablero = np.pad(vista_del_tablero, 1, constant_values="|")
vista_del_tablero[0, :]=np.arange(12)
vista_del_tablero[:, 0]=np.arange(12)
vista_del_tablero[11, :]=np.full((1,12), "|")
vista_del_tablero[:, 11]=np.full((1,12), "|")


disparos_anteriores = {"agua":set(), "tocado":[]}  # y tambien celdas alrededor de barcos hundidos
flota={"barco4":[], "barco3":[], "barco2":[], "barco1":[]}

colocar_10_barcos_rand(tablero)
orient_buscar = None
tocado=False
es4=False

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



disparar_rand(tablero, vista_del_tablero, disparos_anteriores, orient_buscar, tocado, es4)
print(tablero)
print("set de disparos anteriores: ", disparos_anteriores)    
print(vista_del_tablero)


disparar_rand(tablero, vista_del_tablero, disparos_anteriores, orient_buscar, tocado, es4)
print(tablero)
print("set de disparos anteriores: ", disparos_anteriores)    
print(vista_del_tablero)


disparar_rand(tablero, vista_del_tablero, disparos_anteriores, orient_buscar, tocado, es4)
print(tablero)
print("set de disparos anteriores: ", disparos_anteriores)    
print(vista_del_tablero)

disparar_rand(tablero, vista_del_tablero, disparos_anteriores, orient_buscar, tocado, es4)
print(tablero)
print("set de disparos anteriores: ", disparos_anteriores)    
print(vista_del_tablero)


disparar_rand(tablero, vista_del_tablero, disparos_anteriores, orient_buscar, tocado, es4)
print(tablero)
print("set de disparos anteriores: ", disparos_anteriores)    
print(vista_del_tablero)


disparar_rand(tablero, vista_del_tablero, disparos_anteriores, orient_buscar, tocado, es4)
print(tablero)
print("set de disparos anteriores: ", disparos_anteriores)    
print(vista_del_tablero)
disparar_rand(tablero, vista_del_tablero, disparos_anteriores, orient_buscar, tocado, es4)
print(tablero)
print("set de disparos anteriores: ", disparos_anteriores)    
print(vista_del_tablero)


disparar_rand(tablero, vista_del_tablero, disparos_anteriores, orient_buscar, tocado, es4)
print(tablero)
print("set de disparos anteriores: ", disparos_anteriores)    
print(vista_del_tablero)


disparar_rand(tablero, vista_del_tablero, disparos_anteriores, orient_buscar, tocado, es4)
print(tablero)
print("set de disparos anteriores: ", disparos_anteriores)    
print(vista_del_tablero)
disparar_rand(tablero, vista_del_tablero, disparos_anteriores, orient_buscar, tocado, es4)
print(tablero)
print("set de disparos anteriores: ", disparos_anteriores)    
print(vista_del_tablero)


disparar_rand(tablero, vista_del_tablero, disparos_anteriores, orient_buscar, tocado, es4)
print(tablero)
print("set de disparos anteriores: ", disparos_anteriores)    
print(vista_del_tablero)


disparar_rand(tablero, vista_del_tablero, disparos_anteriores, orient_buscar, tocado, es4)
print(tablero)
print("set de disparos anteriores: ", disparos_anteriores)    
print(vista_del_tablero)