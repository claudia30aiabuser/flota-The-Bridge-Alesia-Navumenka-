import numpy as np
import random


def crear_tablero(size=10, vista=False):

    tablero=np.full((size+2, size+2), ".")
    tablero[0, :]=np.arange(size+2)
    tablero[:, 0]=np.arange(size+2)
    tablero[-1, :]=np.full((1,size+2), "1")
    tablero[:, -1]=np.full((1,size+2), "1")

    vista_del_tablero = np.full((size+2, size+2), ".")
    vista_del_tablero[0, :]=np.arange(size+2)
    vista_del_tablero[:, 0]=np.arange(size+2)
    vista_del_tablero[-1, :]=np.full((1,size+2), "1")
    vista_del_tablero[:, -1]=np.full((1,size+2), "1")

    if vista == False:
        return tablero
    elif vista == True:
        return vista_del_tablero


def colocar_barcos(tablero, *mi_flota):
    if mi_flota == 0:
        mi_flota = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        return colocar_barcos_rand(tablero, mi_flota)
    else:
        return colocar_barcos_rand(tablero, mi_flota)



def colocar_barcos_rand(tablero, *mi_flota):


    def colocar_barco4_rand(tablero):

        # pin4fil, pin4col - punto 2 del barco [][*][][]
        orient4 =np.random.choice(["vert", "horiz"]) 
    
        if orient4 == "vert":
            pin4fil =np.random.randint(2,9) # fila de "cabeza" del barco 4
            pin4col =np.random.randint(1,11) # columna de "cabeza" del barco 4

            choca = np.any(tablero[pin4fil-1:pin4fil+3, pin4col] == "■") or np.any(tablero[pin4fil-1:pin4fil+3, pin4col] == "~")

            if choca == False: 
                tablero[pin4fil-1:pin4fil+3, pin4col]="■" 
                
                tablero[pin4fil-2:pin4fil+4, pin4col+1]="~" 
                tablero[pin4fil-2:pin4fil+4, pin4col-1]="~" 
                tablero[pin4fil-2, pin4col]="~" 
                tablero[pin4fil+3, pin4col]="~" 
            else: colocar_barco4_rand(tablero)

        elif orient4 == "horiz": 
            pin4fil =np.random.randint(1,11)    
            pin4col =np.random.randint(2,9)   

            choca = np.any(tablero[pin4fil, pin4col-1:pin4col+3] == "■") or np.any(tablero[pin4fil, pin4col-1:pin4col+3] == "~") 

            if choca == False:
                tablero[pin4fil, pin4col-1:pin4col+3]="■"
            
                tablero[pin4fil, pin4col-2]="~"
                tablero[pin4fil, pin4col+3]="~"
                tablero[pin4fil+1, pin4col-2:pin4col+4]="~"
                tablero[pin4fil-1, pin4col-2:pin4col+4]="~"
            else: colocar_barco4_rand(tablero)

    def colocar_barco3_rand(tablero):

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
            else: colocar_barco3_rand(tablero)

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
            else: colocar_barco3_rand(tablero)


    def colocar_barco2_rand(tablero):
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
            else: colocar_barco2_rand(tablero)

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
            else: colocar_barco2_rand(tablero)


    def colocar_barco1_rand(tablero):
        
        pin1fil =np.random.randint(1,11) 
        pin1col =np.random.randint(1,11)  

        choca = np.any(tablero[pin1fil, pin1col] == "■") or np.any(tablero[pin1fil, pin1col] == "~")

        if choca == False: 
            tablero[pin1fil, pin1col] = "■"

            tablero[pin1fil-1, pin1col-1 : pin1col+2] = "~"
            tablero[pin1fil+1, pin1col-1 : pin1col+2] = "~"
            tablero[pin1fil, pin1col-1] = "~"
            tablero[pin1fil, pin1col+1] = "~"
        else: colocar_barco1_rand(tablero)

    colocar_barco4_rand(tablero) # uno de 4
    colocar_barco3_rand(tablero) # dos de 3
    colocar_barco3_rand(tablero)
    colocar_barco2_rand(tablero) # tres de 2
    colocar_barco2_rand(tablero)
    colocar_barco2_rand(tablero)
    colocar_barco1_rand(tablero) # cuatro de 1
    colocar_barco1_rand(tablero)
    colocar_barco1_rand(tablero)
    colocar_barco1_rand(tablero)

    # bordes de tablero bonitos
    tablero[0, :]=np.arange(12)
    tablero[:, 0]=np.arange(12)
    tablero[11, :]=np.full((1,12), "|")
    tablero[:, 11]=np.full((1,12), "|")


def disparar((dfil, dcol), tablero):


def disparar_rand(tablero):