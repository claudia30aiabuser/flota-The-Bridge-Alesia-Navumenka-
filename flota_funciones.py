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

def hundir(matriz, disparos_anteriores, *pos_seq, orient_buscar=None, orient_buscar_exact=None):  # solo para facilitarme los slicings de pads de barcos hundidos
     # pos_tuple: ( (f1,c1),(f2,c2),(f3,c3),(f4,c4) )
    if orient_buscar == "horiz":

        #lista sorteada de casillas del barco
        #max: [(3, 1), (3, 2), (3, 3), (3, 4)]
        barco=sorted(list(i for i in pos_seq))
            #fila arriba:
        matriz[barco[0][0]-1, barco[0][1]-1 : barco[-1][1]+2] = "~" 
        alrededores=list( (f-1, c) for f,c in barco )
        disparos_anteriores["agua"].update(alrededores) 
        disparos_anteriores["agua"].add((barco[0][0]-1, barco[0][1]-1)) 
        disparos_anteriores["agua"].add((barco[-1][0]-1, barco[-1][1]+1))    
            #fila abajo:
        matriz[barco[0][0]+1, barco[0][1]-1 : barco[-1][1]+2] = "~"  
        alrededores=list((f+1, c) for f,c in barco)
        disparos_anteriores["agua"].update(alrededores)
        disparos_anteriores["agua"].add((barco[0][0]+1, barco[0][1]-1)) 
        disparos_anteriores["agua"].add((barco[-1][0]+1, barco[-1][1]+1)) 
            #casillas de lados 
        matriz[barco[0][0], barco[0][1]-1] = "~"
        disparos_anteriores["agua"].add((barco[0][0], barco[0][1]-1))
        matriz[barco[0][0], barco[-1][1]+1] = "~"
        disparos_anteriores["agua"].add((barco[0][0], barco[-1][1]+1))
             
    elif orient_buscar == "vert":
        # max: [(1, 2), (2, 2), (3, 2), (4, 2)]
        barco=sorted(list(i for i in pos_seq))
            #columna izq:
        matriz[barco[0][0]-1 : barco[-1][0]+2, barco[0][1]-1 ] = "~" 
        alrededores=list( (f, c-1) for f,c in barco )
        disparos_anteriores["agua"].update(alrededores) 
        disparos_anteriores["agua"].add((barco[0][0]-1, barco[0][1]-1)) 
        disparos_anteriores["agua"].add((barco[-1][0]+1, barco[-1][1]-1))    
            #columna der:
        matriz[barco[0][0]-1 : barco[-1][0]+2, barco[0][1]+1] = "~"  
        alrededores=list((f, c+1) for f,c in barco)
        disparos_anteriores["agua"].update(alrededores)
        disparos_anteriores["agua"].add((barco[0][0]-1, barco[0][1]+1)) 
        disparos_anteriores["agua"].add((barco[-1][0]+1, barco[-1][1]+1)) 
            #casillas de puntas 
        matriz[barco[0][0]-1, barco[0][1]] = "~"
        disparos_anteriores["agua"].add((barco[0][0]-1, barco[0][1]))
        matriz[barco[-1][0]+1, barco[-1][1]] = "~"
        disparos_anteriores["agua"].add((barco[-1][0]+1, barco[-1][1]))
        
    else:
        # entonces fue un barco de 1: (pos_seq[0][0], pos_seq[0][1])
        matriz[pos_seq[0][0]-1, pos_seq[0][1]-1 : pos_seq[0][1] +2] = "~"
        disparos_anteriores["agua"].add((pos_seq[0][0]-1, pos_seq[0][1]-1))
        disparos_anteriores["agua"].add((pos_seq[0][0]-1, pos_seq[0][1]))
        disparos_anteriores["agua"].add((pos_seq[0][0]-1, pos_seq[0][1]+1))
        
        matriz[pos_seq[0][0]+1, pos_seq[0][1]-1 : pos_seq[0][1] +2] = "~"
        disparos_anteriores["agua"].add((pos_seq[0][0]+1, pos_seq[0][1]-1))
        disparos_anteriores["agua"].add((pos_seq[0][0]+1, pos_seq[0][1]))
        disparos_anteriores["agua"].add((pos_seq[0][0]+1, pos_seq[0][1]+1))

        matriz[pos_seq[0][0], pos_seq[0][1]-1] = "~"
        matriz[pos_seq[0][0], pos_seq[0][1]+1] = "~"
        disparos_anteriores["agua"].add((pos_seq[0][0], pos_seq[0][1]-1))
        disparos_anteriores["agua"].add((pos_seq[0][0], pos_seq[0][1]+1))
    
        

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
            disparos_anteriores["agua"].add((disp_fil, disp_col))
          
        elif tablero[disp_fil, disp_col] == ".":
            tablero[disp_fil, disp_col]="A"
            vista_del_tablero[disp_fil, disp_col]="A"
            disparos_anteriores["agua"].add((disp_fil, disp_col))

        elif tablero[disp_fil, disp_col] == "■":
           tablero[disp_fil, disp_col]="X"
           vista_del_tablero[disp_fil, disp_col]="X"
           disparos_anteriores["tocado"].append((disp_fil, disp_col))
           print(">>>>>----Puedo hacer otro disparo----->>>>>")

           # esto es para buscar otras casillas del barco tocado en el disparo anterior o turno anterior   
           if tocado == False:
                # busqueda random de cruz
                if ( tablero[disp_fil-1, disp_col] == "■" or tablero[disp_fil+1, disp_col] == "■" or
                        tablero[disp_fil, disp_col-1] == "■" or tablero[disp_fil, disp_col+1] == "■" ):

                        busco_fil, busco_col = random.choice([(disp_fil, disp_col-1), (disp_fil, disp_col+1),
                                                            (disp_fil+1, disp_col), (disp_fil-1, disp_col)])
                                 
                        print("========= disparo de BUSQUEDA =======\n" \
                                "============   ", (busco_fil, busco_col), "   =============")
                        
                        validacion_barco(busco_fil, busco_col, orient_buscar, orient_buscar_exact, tocado)

           elif tocado == True:
                # busqueda precisa -> se mira a los disparos anteriores para obtener orientacion del barco tocado
                
                
                        fil2, col2 = (disparos_anteriores["tocado"][-2][0], disparos_anteriores["tocado"][-2][1])  

                        if fil2 == disp_fil:
                            orient_buscar == "horiz"

                            busco_fil, busco_col = random.choice([(fil2, col2-1), (disp_fil, disp_col+1)])
                                        
                            print("========= disparo de BUSQUEDA =======\n" \
                                    "============   ", (busco_fil, busco_col), "   =============")
                            
                            validacion_barco(busco_fil, busco_col, orient_buscar, orient_buscar_exact, tocado)                   
                            
                        elif col2 == disp_col: 
                            orient_buscar == "vert"

                            busco_fil, busco_col = random.choice([(fil2+1, col2), (disp_fil-1, disp_col)])
                            disparos_anteriores.append((busco_fil, busco_col))               
                            print("========= disparo de BUSQUEDA =======\n" \
                                    "============   ", (busco_fil, busco_col), "   =============")
                            
                            validacion_barco(busco_fil, busco_col, orient_buscar, orient_buscar_exact, tocado) 
                    
                    

                if ( tablero[fil2-1, col2] == "■" or tablero[fil2+1, col2] == "■" or
                                tablero[fil2, col2-1] == "■" or tablero[fil2, col2+1] == "■" ):
                    
                    busco_fil, busco_col = random.choice([(disp_fil, disp_col-1), (disp_fil, disp_col+1),
                                                        (disp_fil+1, disp_col), (disp_fil-1, disp_col)])
                    disparos_anteriores.append((busco_fil, busco_col))               
                    print("========= disparo de BUSQUEDA =======\n" \
                            "============   ", (busco_fil, busco_col), "   =============")
                    
                    validacion_barco(busco_fil, busco_col, orient_buscar, orient_buscar_exact, tocado)               


    def validacion_barco(disp_fil, disp_col, orient_buscar=None, orient_buscar_exact=None, tocado=False):

        if tocado == False: # aqui se entra al acertar primer X 
                            
           if ( tablero[disp_fil-1, disp_col] == "■" or tablero[disp_fil+1, disp_col] == "■" or
                tablero[disp_fil, disp_col-1] == "■" or tablero[disp_fil, disp_col+1] == "■" ):

                tocado=True
                busco_fil, busco_col = random.choice([(disp_fil, disp_col-1), (disp_fil, disp_col+1),
                                                    (disp_fil+1, disp_col), (disp_fil-1, disp_col)])
                            
                print("========= disparo de BUSQUEDA =======\n" \
                        "============   ", (busco_fil, busco_col), "   =============")
                validacion_disparos(busco_fil, busco_col, orient_buscar, orient_buscar_exact, tocado)

           else:
                hundir(vista_del_tablero, disparos_anteriores, disp_fil, disp_col)
                print("---------¡¡¡ BARCO de 1 HUNDIDO !!!---------")
                print(" >>>>>----Puedo hacer otro disparo----->>>>>")
                disparar_rand(tablero, vista_del_tablero, disparos_anteriores, tocado)

        elif tocado == True:

           if ( tablero[disp_fil-1, disp_col] == "■" or tablero[disp_fil+1, disp_col] == "■" or
                 tablero[disp_fil, disp_col-1] == "■" or tablero[disp_fil, disp_col+1] == "■" ):   
                # aqui entra un barco de 3 o 4
                fil2, col2 = (disparos_anteriores["tocado"][-2][0], disparos_anteriores["tocado"][-2][1]) 
                
                if orient_buscar == "horiz":
                    busco_fil, busco_col = random.choice([(fil2, col2-1), (disp_fil, disp_col+1)]) 
                    print("========= disparo de BUSQUEDA =======\n" \
                            "============   ", (busco_fil, busco_col), "   =============")
                    validacion_disparos(busco_fil, busco_col, orient_buscar, orient_buscar_exact, tocado)
                     

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
                    print("========= disparo de BUSQUEDA =======\n" \
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

             
    if tocado == True:
        # tomo el disparo del turno previo en el cual habia fallado pero tocado el barco
        fil2, col2 = (disparos_anteriores[-2][0], disparos_anteriores[-2][1])
        disp_fil, disp_col = random.choice((fil2-1, col2), (fil2+1, col2), 
                                           (fil2, col2-1), (fil2, col2+1))
    else: 
        disp_fil = np.random.randint(1, 11)
        disp_col = np.random.randint(1, 11)
    
    print("==============  disparo NUEVO  ===============\n" \
        "================= ", (disp_fil, disp_col), " =================")
   

    if not ((disp_fil, disp_col) in disparos_anteriores):    
       
       validacion_disparos(disp_fil, disp_col, tocado) 

    else: 
        print("Este disparo ya existe - reintento") 
        disparar_rand(tablero, vista_del_tablero, disparos_anteriores, tocado)













