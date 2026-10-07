import numpy as np
#import flota_main

# def crear_tablero():
#     tablero=np.full((12, 12), " ")
#     tablero[0, :]=np.arange(12)
#     tablero[:, 0]=np.arange(12)
#     tablero[11, :]=np.full((1,12), "/")
#     tablero[:, 11]=np.full((1,12), "/")
#     # tablero[0, :]=np.array([chr(8304), chr(185), chr(178), chr(179), chr(8308), chr(8309), chr(8310), chr(8311), chr(8312), chr(8313), chr(7496), "*"])
#     # tablero[:, 0]=np.array([chr(8304), chr(185), chr(178), chr(179), chr(8308), chr(8309), chr(8310), chr(8311), chr(8312), chr(8313), chr(7496), "*"])
#     # #tablero[11, :]=np.full((1, 11), "*") 
#     vista_del_tablero = np.full((10, 10), " ")
#     vista_del_tablero = np.pad(vista_del_tablero, 1, constant_values="/")
#     print(tablero)
#     print(vista_del_tablero)

# crear_tablero()

tablero=np.full((12, 12), ".")
tablero[0, :]=np.arange(12)
tablero[:, 0]=np.arange(12)
tablero[11, :]=np.full((1,12), "|")
tablero[:, 11]=np.full((1,12), "|")
        # tablero[0, :]=np.array([chr(8304), chr(185), chr(178), chr(179), chr(8308), chr(8309), chr(8310), chr(8311), chr(8312), chr(8313), chr(7496), "*"])
        # tablero[:, 0]=np.array([chr(8304), chr(185), chr(178), chr(179), chr(8308), chr(8309), chr(8310), chr(8311), chr(8312), chr(8313), chr(7496), "*"])
        # #tablero[11, :]=np.full((1, 11), "*") 
vista_del_tablero = np.full((10, 10), ".")
vista_del_tablero = np.pad(vista_del_tablero, 1, constant_values="|")
vista_del_tablero[0, :11]=np.arange(11)
vista_del_tablero[:11, 0]=np.arange(11)
# print(tablero)
# print(vista_del_tablero)
 
def colocar_barco4_rand():
   
    # primero se coloca el barco mas largo al azar
    # no compruebo choques 
    # pin4fil, pin4col - punto 2 del barco [][*][][]
    orient4 =np.random.choice(["vert", "horiz"]) 
   
    if orient4 == "vert":
        pin4fil =np.random.randint(2,9) # fila de "cabeza" del barco 4
        pin4col =np.random.randint(1,11) # columna de "cabeza" del barco 4
        print("orient4 =", orient4, "| fila4 =", pin4fil, "| columna4 =", pin4col) #quitar el print
        tablero[pin4fil-1:pin4fil+3, pin4col]="■" 
        
        tablero[pin4fil-2:pin4fil+4, pin4col+1]="~" 
        tablero[pin4fil-2:pin4fil+4, pin4col-1]="~" 
        tablero[pin4fil-2, pin4col]="~" 
        tablero[pin4fil+3, pin4col]="~" 
    elif orient4 == "horiz": 
        pin4fil =np.random.randint(1,11)    
        pin4col =np.random.randint(2,9)    
        print("orient4 =", orient4, "| fila4 =", pin4fil, "| columna4 =", pin4col) #quitar el print
        tablero[pin4fil, pin4col-1:pin4col+3]="■"
        
        tablero[pin4fil, pin4col-2]="~"
        tablero[pin4fil, pin4col+3]="~"
        tablero[pin4fil+1, pin4col-2:pin4col+4]="~"
        tablero[pin4fil-1, pin4col-2:pin4col+4]="~"
   

def colocar_barco3_rand():

    # pin3fil, pin3col - punto 2 del barco [][*][]
    orient3 =np.random.choice(["vert", "horiz"]) 
        
    if orient3 == "horiz":

        pin3fil =np.random.randint(1,10) 
        pin3col =np.random.randint(2,10)  
        # print("orient3 =", orient3, "fila3 =", pin3fil, " columna3 =", pin3col) #quitar el print
        choca = np.any(tablero[pin3fil, pin3col-1 : pin3col+2] == "■") or np.any(tablero[pin3fil, pin3col-1 : pin3col+2] == "~")

        if choca == False: 
            tablero[pin3fil, pin3col-1 : pin3col+2] = "■"
            # dibujo ~ alrededor
            tablero[pin3fil, pin3col-2] = "~"
            tablero[pin3fil, pin3col+2] = "~"
            tablero[pin3fil-1, pin3col-2 : pin3col+3] = "~"
            tablero[pin3fil+1, pin3col-2 : pin3col+3] = "~"
        else: colocar_barco3_rand()

    elif orient3 == "vert":

        pin3fil =np.random.randint(2,10) 
        pin3col =np.random.randint(1,11) 
        # print("orient3 =", orient3, "fila3 =", pin3fil, " columna3 =", pin3col) #quitar el print
        choca = np.any(tablero[pin3fil-1:pin3fil+2, pin3col] == "■") or np.any(tablero[pin3fil-1:pin3fil+2, pin3col] == "~")

        if choca == False: 
            tablero[pin3fil-1:pin3fil+2, pin3col] = "■"
            # dibujo ~ alrededor
            tablero[pin3fil-2:pin3fil+3, pin3col-1] = "~"
            tablero[pin3fil-2:pin3fil+3, pin3col+1] = "~"
            tablero[pin3fil-2, pin3col] = "~"
            tablero[pin3fil+2, pin3col] = "~"
        else: colocar_barco3_rand()


def colocar_barco2_rand():
    # pin2fil, pin2col - punto 1 del barco [*][]
    orient2 =np.random.choice(["vert", "horiz"]) 
        
    if orient2 == "horiz":

        pin2fil =np.random.randint(1,11) 
        pin2col =np.random.randint(1,10)  
        # print("orient2 =", orient2, "fila2 =", pin2fil, " columna2 =", pin2col) #quitar el print
        choca = np.any(tablero[pin2fil, pin2col : pin2col+2] == "■") or np.any(tablero[pin2fil, pin2col : pin2col+2] == "~")

        if choca == False: 
            tablero[pin2fil, pin2col : pin2col+2] = "■"
            
            tablero[pin2fil+1, pin2col-1 : pin2col+3] = "~"
            tablero[pin2fil-1, pin2col-1 : pin2col+3] = "~"
            tablero[pin2fil, pin2col+2] = "~"
            tablero[pin2fil, pin2col-1] = "~"
        else: colocar_barco2_rand()

    if orient2 == "vert":

        pin2fil =np.random.randint(1,10) 
        pin2col =np.random.randint(1,11)  
        # print("orient2 =", orient2, "fila2 =", pin2fil, " columna2 =", pin2col) #quitar el print
        choca = np.any(tablero[pin2fil : pin2fil+2, pin2col] == "■") or np.any(tablero[pin2fil : pin2fil+2, pin2col] == "~")

        if choca == False: 
            tablero[pin2fil : pin2fil+2, pin2col] = "■"

            tablero[pin2fil-1 : pin2fil+3, pin2col+1] = "~"
            tablero[pin2fil-1 : pin2fil+3, pin2col-1] = "~"
            tablero[pin2fil-1, pin2col] = "~"
            tablero[pin2fil+2, pin2col] = "~"
        else: colocar_barco2_rand()


def colocar_barco1_rand():
    
    pin1fil =np.random.randint(1,11) 
    pin1col =np.random.randint(1,11)  

    choca = np.any(tablero[pin1fil, pin1col] == "■") or np.any(tablero[pin1fil, pin1col] == "~")

    if choca == False: 
        tablero[pin1fil, pin1col] = "■"

        tablero[pin1fil-1, pin1col-1 : pin1col+2] = "~"
        tablero[pin1fil+1, pin1col-1 : pin1col+2] = "~"
        tablero[pin1fil, pin1col-1] = "~"
        tablero[pin1fil, pin1col+1] = "~"
    else: colocar_barco1_rand()

#crear_tablero()

colocar_barco4_rand()

colocar_barco3_rand()
colocar_barco3_rand()

colocar_barco2_rand()
colocar_barco2_rand()
colocar_barco2_rand()

colocar_barco1_rand()
colocar_barco1_rand()
colocar_barco1_rand()
colocar_barco1_rand()

print("==================NUEVA=PARTIDA==================NUEVA=PARTIDA===================NUEVA=PARTIDA==\n" \
      "==NUEVA=PARTIDA==================NUEVA=PARTIDA===================NUEVA=PARTIDA==================\n" \
      "==================NUEVA=PARTIDA==================NUEVA=PARTIDA===================NUEVA=PARTIDA==")
print(tablero)    
print("Como se ve mi tablero:")
print(vista_del_tablero)


paso_turno=bool

def disparar():
 
    disp_fil = np.random.randint(1, 11)
    disp_col = np.random.randint(1, 11)
    print("=============disparo=================\n" \
          "==============nuevo==================\n" \
          "==========   ", (disp_fil, disp_col), "   ==========")
   

    if not ((disp_fil, disp_col) in disparos_anteriores):    
       disparos_anteriores.add((disp_fil, disp_col))

       if tablero[disp_fil, disp_col] == "~":
            tablero[disp_fil, disp_col]="A"
            vista_del_tablero[disp_fil, disp_col]="A"
          
       elif tablero[disp_fil, disp_col] == ".":
            tablero[disp_fil, disp_col]="A"
            vista_del_tablero[disp_fil, disp_col]="A"

       elif tablero[disp_fil, disp_col] == "■":
           tablero[disp_fil, disp_col]="X"
           vista_del_tablero[disp_fil, disp_col]="X"
           print("Puedo hacer otro disparo")
           
        #    if ( tablero[disp_fil-1, disp_col] == "■" or tablero[disp_fil+1, disp_col] == "■" or
        #        tablero[disp_fil, disp_col-1] == "■" or tablero[disp_fil, disp_col+1] == "■" ):
                   
        #            (busco_fil, busco_col) = np.random.randchoice((disp_fil-1, disp_col), (disp_fil+1, disp_col),
        #                                                           (disp_fil, disp_col-1), (disp_fil, disp_col+1))
        #            disparos_anteriores.add((busco_fil, busco_col))
        #            print("=============disparo=de================\n" \
        #                 "==============busqueda==================\n" \
        #                 "==========   ", (busco_fil, busco_col), "   ==========")
        #            # y despues que? hay que entrar en la funcion pero desde 2do elif o reescribirlos aqui
        #    else: disparar()
               

    else: disparar()


disparos_anteriores = set()

disparar()
print(tablero)
print("set de disparos anteriores: ", disparos_anteriores)    
print(vista_del_tablero)

disparar()
print(tablero)
print("set de disparos anteriores: ", disparos_anteriores)    
print(vista_del_tablero)

disparar()
print(tablero)
print("set de disparos anteriores: ", disparos_anteriores)  
print(vista_del_tablero)

disparar()
print(tablero)
print("set de disparos anteriores: ", disparos_anteriores)     
print(vista_del_tablero)

disparar()
print(tablero)
print("set de disparos anteriores: ", disparos_anteriores)   
print(vista_del_tablero)

disparar()
print(tablero)
print("set de disparos anteriores: ", disparos_anteriores)     
print(vista_del_tablero)

disparar()
print(tablero)
print("set de disparos anteriores: ", disparos_anteriores)     
print(vista_del_tablero)

disparar()
print(tablero)
print("set de disparos anteriores: ", disparos_anteriores)     
print(vista_del_tablero)

disparar()
print(tablero)
print("set de disparos anteriores: ", disparos_anteriores)     
print(vista_del_tablero)

disparar()
print(tablero)
print("set de disparos anteriores: ", disparos_anteriores)     
print(vista_del_tablero)








