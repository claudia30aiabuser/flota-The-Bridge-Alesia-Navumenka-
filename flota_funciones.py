import numpy as np
import random

# def crear_tablero(tablero, ocultado=False):
#     tablero=np.full((12, 12), ".")
#     tablero[0, :]=np.arange(12)
#     tablero[:, 0]=np.arange(12)
#     tablero[11, :]=np.full((1,12), "|")
#     tablero[:, 11]=np.full((1,12), "|")

#     ocultado = np.full((10, 10), ".")
#     ocultado = np.pad(ocultado, 1, constant_values="|")
#     ocultado[0, :11]=np.arange(11)
#     ocultado[:11, 0]=np.arange(11)

#     if ocultado == True:
#         return ocultado
#     else:
#         return tablero

def hundir(matriz, *pos_seq, orient_buscar=None, orient_buscar_exact=None):  # solo para facilitarme los slicings de pads de barcos hundidos
     # pos_tuple: ( (f1,c1),(f2,c2),(f3,c3),(f4,c4) )
    if orient_buscar == "horiz":
        
        max_col = max(i[1] for i in pos_seq)
        min_col = min(i[1] for i in pos_seq)

        matriz[pos_seq[0][0]-1 : pos_seq[0][0]+2 , min_col-1 : max_col+2] = "~"
        matriz[pos_seq[0][0], min_col : max_col+1] = "X"
             
    elif orient_buscar == "vert":

        max_fil = max(i[0] for i in pos_seq)
        min_fil = min(i[0] for i in pos_seq)

        matriz[min_fil-1 : max_fil+2 , pos_seq[0][1]-1 : pos_seq[0][1]+2] = "~"
        matriz[min_fil : max_fil+1, pos_seq[0][1]] = "X"
        
    else:
        # entonces fue un barco de 1
        matriz[pos_seq[0][0]-1 : pos_seq[0][0]+2 , pos_seq[0][1]-1 : pos_seq[0][1]+2] = "~"
        matriz[pos_seq[0][0], pos_seq[0][1]] = "X"
    
        

      

def colocar_10_barcos_rand(tablero):

    def colocar_barco4_rand(tablero):
    
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


def disparar_rand(tablero, vista_del_tablero, disparos_anteriores, tocado=False):
 
    def validacion_disparos(disp_fil, disp_col, orient_buscar=None, orient_buscar_exact=None, tocado=False):
        
        if tablero[disp_fil, disp_col] == "~":
            tablero[disp_fil, disp_col]="A"
            vista_del_tablero[disp_fil, disp_col]="A"
          
        elif tablero[disp_fil, disp_col] == ".":
            tablero[disp_fil, disp_col]="A"
            vista_del_tablero[disp_fil, disp_col]="A"

        elif tablero[disp_fil, disp_col] == "■":
           tablero[disp_fil, disp_col]="X"
           vista_del_tablero[disp_fil, disp_col]="X"
           # esto es para buscar otras casillas del barco tocado en el disparo anterior o turno anterior   
          
           if tocado == False:
                # busqueda random de cruz
                if ( tablero[disp_fil-1, disp_col] == "■" or tablero[disp_fil+1, disp_col] == "■" or
                        tablero[disp_fil, disp_col-1] == "■" or tablero[disp_fil, disp_col+1] == "■" ):

                        busco_fil, busco_col = random.choice([(disp_fil, disp_col-1), (disp_fil, disp_col+1),
                                                            (disp_fil+1, disp_col), (disp_fil-1, disp_col)])
                        disparos_anteriores.append((busco_fil, busco_col))               
                        print("=============disparo=de================\n" \
                                "==============busqueda==================\n" \
                                "============   ", (busco_fil, busco_col), "   =============")
                        
                        validacion_hundir(busco_fil, busco_col, orient_buscar, orient_buscar_exact, tocado)
           elif tocado == True:
                # busqueda precisa -> se mira a los disparos anteriores para obtener orientacion del barco tocado
                fil2, col2 = (disparos_anteriores[-2][0], disparos_anteriores[-2][1])  

                if fil2 == disp_fil:
                    orient_buscar == "horiz"

                    busco_fil, busco_col = random.choice([(fil2, col2-1), (disp_fil, disp_col+1)])
                    disparos_anteriores.append((busco_fil, busco_col))               
                    print("=============disparo=de================\n" \
                            "==============busqueda==================\n" \
                            "============   ", (busco_fil, busco_col), "   =============")
                    
                    validacion_hundir(busco_fil, busco_col, orient_buscar, orient_buscar_exact, tocado)                   
                    
                elif col2 == disp_col: 
                    orient_buscar == "vert"

                    busco_fil, busco_col = random.choice([(fil2+1, col2), (disp_fil-1, disp_col)])
                    disparos_anteriores.append((busco_fil, busco_col))               
                    print("=============disparo=de================\n" \
                            "==============busqueda==================\n" \
                            "============   ", (busco_fil, busco_col), "   =============")
                    
                    validacion_hundir(busco_fil, busco_col, orient_buscar, orient_buscar_exact, tocado) 
                    
                    

                if ( tablero[fil2-1, col2] == "■" or tablero[fil2+1, col2] == "■" or
                                tablero[fil2, col2-1] == "■" or tablero[fil2, col2+1] == "■" ):
                    
                    busco_fil, busco_col = random.choice([(disp_fil, disp_col-1), (disp_fil, disp_col+1),
                                                        (disp_fil+1, disp_col), (disp_fil-1, disp_col)])
                    disparos_anteriores.append((busco_fil, busco_col))               
                    print("=============disparo=de================\n" \
                            "==============busqueda==================\n" \
                            "============   ", (busco_fil, busco_col), "   =============")
                    
                    validacion_hundir(busco_fil, busco_col, orient_buscar, orient_buscar_exact, tocado)               
                   
                   
                             
                   if orient_buscar is None:
                       orient_buscar =random.choice(["vert", "horiz"]) 
                   else: pass   # en caso de barcos de 3 o 4 ya estaria definido 


                   if orient_buscar == "horiz":
                        # esto puede disparar al borde - solucionarlo con try/except
                        if tablero[disp_fil, disp_col-1] == "X":  #solo para barcos horizontales de 3 o 4 en su 3r o 4to disparo
                            busco_fil, busco_col = disp_fil, disp_col+1
                            disparos_anteriores.append((busco_fil, busco_col)) 
                            orient_buscar_exact = "right"    #me sirve para hundir barco luego
                            print("=============disparo=de================\n" \
                                "==============busqueda==================\n" \
                                "============   ", (busco_fil, busco_col), "   =============")
                            
                            tocado = True # para el comportamiento de busqueda en siguiente turno si falla el disparo de busqueda
                           
                            validacion_disparos(busco_fil, busco_col, orient_buscar, orient_buscar_exact, tocado)
                        elif tablero[disp_fil, disp_col+1] == "X":
                            busco_fil, busco_col = disp_fil, disp_col-1
                            disparos_anteriores.append((busco_fil, busco_col)) 
                            orient_buscar_exact = "left"
                            print("=============disparo=de================\n" \
                                "==============busqueda==================\n" \
                                "============   ", (busco_fil, busco_col), "   =============")

                            tocado = True

                            validacion_disparos(busco_fil, busco_col, orient_buscar, orient_buscar_exact, tocado)
                        else: # si entra aqui es un barco horizontal de 2/3/4 en su 2do disparo 
                            busco_fil, busco_col = random.choice([(disp_fil, disp_col-1), (disp_fil, disp_col+1)])
                            disparos_anteriores.append((busco_fil, busco_col))               
                            print("=============disparo=de================\n" \
                                    "==============busqueda==================\n" \
                                    "============   ", (busco_fil, busco_col), "   =============")
                            
                            tocado = True

                            validacion_disparos(busco_fil, busco_col, orient_buscar, orient_buscar_exact, tocado)

                   elif orient_buscar == "vert":

                        if tablero[disp_fil-1, disp_col] == "X":  #solo para barcos verticales de 3 o 4 en su 3r o 4to disparo
                            busco_fil, busco_col = disp_fil+1, disp_col
                            disparos_anteriores.append((busco_fil, busco_col)) 
                            orient_buscar_exact = "up"    #me sirve para hundir barco luego
                            print("=============disparo=de================\n" \
                                "==============busqueda==================\n" \
                                "============   ", (busco_fil, busco_col), "   =============")

                            tocado = True

                            validacion_disparos(busco_fil, busco_col, orient_buscar, orient_buscar_exact, tocado)
                        elif tablero[disp_fil+1, disp_col] == "X":
                            busco_fil, busco_col = disp_fil-1, disp_col
                            disparos_anteriores.append((busco_fil, busco_col)) 
                            orient_buscar_exact = "down"
                            print("=============disparo=de================\n" \
                                "==============busqueda==================\n" \
                                "============   ", (busco_fil, busco_col), "   =============")

                            tocado = True 

                            validacion_disparos(busco_fil, busco_col, orient_buscar, orient_buscar_exact, tocado)
                        else: # si entra aqui es un barco vertical de 2/3/4 en su 2do disparo 
                            busco_fil, busco_col = random.choice([(disp_fil-1, disp_col), (disp_fil+1, disp_col)])
                            disparos_anteriores.append((busco_fil, busco_col))  
                                     
                            print("=============disparo=de================\n" \
                                    "==============busqueda==================\n" \
                                    "============   ", (busco_fil, busco_col), "   =============")
                            
                            tocado = True

                            validacion_disparos(busco_fil, busco_col, orient_buscar, orient_buscar_exact, tocado)
           else:   # para barcos hundidos de 1

                for f, l in [(disp_fil-1, disp_col), (disp_fil+1, disp_col), (disp_fil, disp_col-1),
                                                                             (disp_fil, disp_col+1)]:
                    vista_del_tablero[f, l] = "~"
                    disparos_anteriores.append((f, l))
                
                print("----¡¡¡¡¡¡¡¡¡¡ BARCO HUNDIDO !!!!!!!!!!----")
                print(">>>>>----Puedo hacer otro disparo----->>>>>")
                disparar_rand(tablero, vista_del_tablero, disparos_anteriores, tocado)

    def validacion_hundir(disp_fil, disp_col, orient_buscar=None, orient_buscar_exact=None, tocado=False):
                  
           if ( tablero[disp_fil-1, disp_col] == "■" or tablero[disp_fil+1, disp_col] == "■" or
                tablero[disp_fil, disp_col-1] == "■" or tablero[disp_fil, disp_col+1] == "■" ):

                tocado=True
                print(">>>>>----Puedo hacer otro disparo----->>>>>")
                validacion_disparos(disp_fil, disp_col, orient_buscar, orient_buscar_exact, tocado)

           
           elif ( tablero[disp_fil-1, disp_col] == "X" or tablero[disp_fil+1, disp_col] == "X" or
                 tablero[disp_fil, disp_col-1] == "X" or tablero[disp_fil, disp_col+1] == "X" ): 
                
                # la 3ra casilla del barco de 3/4
                fil3, col3 = (disparos_anteriores["tocados"][-3][0], disparos_anteriores["tocados"][-3][1])  

                if orient_buscar == "horiz":
                     
                    if ( tablero[fil3, col3-1] == "■" or tablero[fil3, col3+1] == "■" ):
                         # esto solo es para el barco de 4 en su penultimo disparo
                        print(">>>>>----Puedo hacer otro disparo----->>>>>")
                        validacion_disparos(disp_fil, disp_col, orient_buscar, orient_buscar_exact, tocado)
                    else:
                         #entonces fue un barco de 3 - lo hundo

                   
                    



                    if orient_buscar == "horiz":
                                               
                                                ??????????????    
                    print("=============disparo=de================\n" \
                            "==============busqueda==================\n" \
                            "============   ", (disp_fil, disp_col), "   =============")
                else: pass
   
                if (orient_buscar == "horiz" and orient_buscar_exact is None):  # validacio del 2do disparo de bercos de 2/3/4  
                     
                    vista_del_tablero[disp_fil-1, disp_col] = "~"
                    vista_del_tablero[disp_fil+1, disp_col] = "~"
                    vista_del_tablero[fil2-1, col2] = "~"
                    vista_del_tablero[fil2+1, col2] = "~"
                    disparos_anteriores.extend([(disp_fil-1, disp_col), (disp_fil+1, disp_col), (fil2-1, col2), (fil2+1, col2)])
                    # como no se si la 2da casilla esta a la derecha o izquierda, lo compruebo:
                    if col2 > disp_col:
                        vista_del_tablero[fil2, col2+1] = "~"
                        vista_del_tablero[disp_fil, disp_col-1] = "~"
                        disparos_anteriores.extend([(fil2, col2+1), (disp_fil, disp_col-1)])
                    else: 
                        vista_del_tablero[fil2, col2-1] = "~"
                        vista_del_tablero[disp_fil, disp_col+1] = "~"
                        disparos_anteriores.extend([(fil2, col2-1), (disp_fil, disp_col+1)])
                    
                    orient_buscar=None 
                    tocado = False
                    print("----¡¡¡¡¡¡¡¡¡¡ BARCO HUNDIDO !!!!!!!!!!----")
                    print(">>>>>----Puedo hacer otro disparo----->>>>>")
                    disparar_rand(tablero, vista_del_tablero, disparos_anteriores, tocado)

                elif (orient_buscar == "vert" and orient_buscar_exact is None):     
                    
                    fil2, col2 = (disparos_anteriores[-2][0], disparos_anteriores[-2][1])
                    
                    vista_del_tablero[disp_fil, disp_col-1] = "~"
                    vista_del_tablero[disp_fil, disp_col+1] = "~"
                    vista_del_tablero[fil2, col2-1] = "~"
                    vista_del_tablero[fil2, col2+1] = "~"
                    disparos_anteriores.extend([(disp_fil, disp_col-1), (disp_fil, disp_col+1), (fil2, col2-1), (fil2, col2+1)])
                    # como no se si la 2da casilla esta arriba o abajo, lo compruebo:
                    if fil2 > disp_fil:
                        vista_del_tablero[fil2+1, col2] = "~"
                        vista_del_tablero[disp_fil-1, disp_col] = "~"
                        disparos_anteriores.extend([(fil2+1, col2), (disp_fil-1, disp_col)])
                    else: 
                        vista_del_tablero[fil2-1, col2] = "~"
                        vista_del_tablero[disp_fil+1, disp_col] = "~"
                        disparos_anteriores.extend([(fil2-1, col2), (disp_fil+1, disp_col)])

                    orient_buscar=None
                    tocado = False 
                    
                    print("----¡¡¡¡¡¡¡¡¡¡ BARCO HUNDIDO !!!!!!!!!!----")
                    print(">>>>>----Puedo hacer otro disparo----->>>>>")
                    disparar_rand(tablero, vista_del_tablero, disparos_anteriores, tocado)
                    
                elif (orient_buscar == "horiz" and orient_buscar_exact == "right"):  # para barcos hundidos de 3 o 4
                    # tambien tengo que distinguir si fue el de 3 o el de 4

                    orient_buscar=None 
                    orient_buscar_exact=None
                    tocado = False
                    
                    print("----¡¡¡¡¡¡¡¡¡¡ BARCO largo HUNDIDO !!!!!!!!!!----")
                    print(">>>>>----Puedo hacer otro disparo----->>>>>")
                    disparar_rand(tablero, vista_del_tablero, disparos_anteriores, tocado)
                elif (orient_buscar == "horiz" and orient_buscar_exact == "left"):
                    
                    orient_buscar=None 
                    orient_buscar_exact=None
                    tocado = False
                    
                    print("----¡¡¡¡¡¡¡¡¡¡ BARCO largo HUNDIDO !!!!!!!!!!----")
                    print(">>>>>----Puedo hacer otro disparo----->>>>>")
                    disparar_rand(tablero, vista_del_tablero, disparos_anteriores,tocado)
                elif (orient_buscar == "vert" and orient_buscar_exact == "up"):
                    
                    orient_buscar=None 
                    orient_buscar_exact=None
                    tocado = False
                    
                    print("----¡¡¡¡¡¡¡¡¡¡ BARCO largo HUNDIDO !!!!!!!!!!----")
                    print(">>>>>----Puedo hacer otro disparo----->>>>>")
                    disparar_rand(tablero, vista_del_tablero, disparos_anteriores, tocado)
                elif (orient_buscar == "vert" and orient_buscar_exact == "down"):
                    
                    orient_buscar=None 
                    orient_buscar_exact=None
                    tocado = False
                    
                    print("----¡¡¡¡¡¡¡¡¡¡ BARCO largo HUNDIDO !!!!!!!!!!----")
                    print(">>>>>----Puedo hacer otro disparo----->>>>>")
                    disparar_rand(tablero, vista_del_tablero, disparos_anteriores, tocado)
             
    if tocado == True:
        # tomo el disparo del turno previo en el cual habia fallado pero toco el barco
        fil2, col2 = (disparos_anteriores[-2][0], disparos_anteriores[-2][1])
        disp_fil, disp_col = random.choice((fil2-1, col2), (fil2+1, col2), 
                                           (fil2, col2-1), (fil2, col2+1))
    else: 
        disp_fil = np.random.randint(1, 11)
        disp_col = np.random.randint(1, 11)
    
    print("=====================disparo======================\n" \
        "======================nuevo=======================\n" \
        "================= ", (disp_fil, disp_col), " =================")
   

    if not ((disp_fil, disp_col) in disparos_anteriores):    
       disparos_anteriores.append((disp_fil, disp_col))
       validacion_disparos(disp_fil, disp_col)             
    else: 
        print("Este disparo ya existe - reintento otra vez") 
        disparar_rand(tablero, vista_del_tablero, disparos_anteriores, tocado)













