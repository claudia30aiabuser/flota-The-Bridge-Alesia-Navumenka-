import numpy as np
import flota_funciones 

# tablero=np.array()
# vista_del_tablero=np.array()

# crear_tablero()

tablero=np.full((12, 12), " ")
tablero[0, :]=np.arange(12)
tablero[:, 0]=np.arange(12)
tablero[11, :]=np.full((1,12), "/")
tablero[:, 11]=np.full((1,12), "/")
# tablero[0, :]=np.array([chr(8304), chr(185), chr(178), chr(179), chr(8308), chr(8309), chr(8310), chr(8311), chr(8312), chr(8313), chr(7496), "*"])
# tablero[:, 0]=np.array([chr(8304), chr(185), chr(178), chr(179), chr(8308), chr(8309), chr(8310), chr(8311), chr(8312), chr(8313), chr(7496), "*"])
# #tablero[11, :]=np.full((1, 11), "*") 
vista_del_tablero = np.full((10, 10), " ")
vista_del_tablero = np.pad(vista_del_tablero, 1, constant_values="/")
print(tablero)
print(vista_del_tablero)

disparos_anteriores = ()
