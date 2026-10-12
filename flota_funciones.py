import numpy as np
import random

# disparos_anteriores = {"agua":{}, "tocados":[]}  # y tambien celdas alrededor de barcos hundidos
# flota={"barco4":[], "barco3":[], "barco2":[], "barco1":[]}

def hundir(matriz, disparos_anteriores, *pos_seq, orient_buscar=None):  # solo para facilitarme los slicings de pads de barcos hundidos
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


def disparar_rand(tablero, vista_del_tablero, disparos_anteriores, orient_buscar=None, tocado=False, es4=False):
 
    def validacion_disparos(disp_fil, disp_col, orient_buscar=None, tocado=False, es4=False):
        
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
           buscar_cerca(disp_fil, disp_col, orient_buscar,  tocado, es4)

          
    def buscar_cerca(disp_fil, disp_col, orient_buscar=None, tocado=False, es4=False):    

        if es4==True:
            fil2, col2 = (disparos_anteriores["tocado"][-2][0], disparos_anteriores["tocado"][-2][1])
            fil3, col3 = (disparos_anteriores["tocado"][-3][0], disparos_anteriores["tocado"][-3][1])
            fil4, col4 = (disparos_anteriores["tocado"][-4][0], disparos_anteriores["tocado"][-4][1])
            hundir(vista_del_tablero, disparos_anteriores, (disp_fil, disp_col) , (fil2, col2), (fil3, col3), (fil4, col4), orient_buscar)
            tocado = False
            orient_buscar = None  
            es4=False          
            print("---------¡¡¡ BARCO de 4 HUNDIDO !!!---------")
            print(" >>>>>----Puedo hacer otro disparo----->>>>>")
            disparar_rand(tablero, vista_del_tablero, disparos_anteriores, orient_buscar, tocado, es4)
        else: pass

        if orient_buscar is None:  # es el 1r o el 2do disparo con resultado "X"
   
           if tocado == False:
                # busqueda random de cruz

                busco_fil, busco_col = random.choice([(disp_fil, disp_col-1), (disp_fil, disp_col+1),
                                                      (disp_fil+1, disp_col), (disp_fil-1, disp_col)])
                            
                print("========= disparo de BUSQUEDA =======\n" \
                        "============   ", (busco_fil, busco_col), "   =============")
                
                validacion_barco(busco_fil, busco_col, orient_buscar, tocado, es4)

           elif tocado == True:
                # busqueda precisa -> se mira a los disparos anteriores para obtener orientacion del barco tocado
                
                        fil2, col2 = (disparos_anteriores["tocado"][-2][0], disparos_anteriores["tocado"][-2][1])  
                        pbarco = sorted(list((disp_fil, disp_col) , (fil2, col2)))

                        if fil2 == disp_fil:
                            orient_buscar == "horiz"

                            busco_fil, busco_col = random.choice([(pbarco[0][0], pbarco[0][1]-1), (pbarco[-1][0], pbarco[-1][1]+1)])
                                        
                            print("========= disparo de BUSQUEDA =======\n" \
                                    "============   ", (busco_fil, busco_col), "   =============")
                            
                            validacion_barco(busco_fil, busco_col, orient_buscar,  tocado, es4)                   
                            
                        elif col2 == disp_col: 
                            orient_buscar == "vert"

                            busco_fil, busco_col = random.choice([(pbarco[0][0]+1, pbarco[0][1]), (pbarco[-1][0]-1, pbarco[-1][1])])
                                        
                            print("========= disparo de BUSQUEDA =======\n" \
                                    "============   ", (busco_fil, busco_col), "   =============")
                            
                            validacion_barco(busco_fil, busco_col, orient_buscar,  tocado, es4)             

        else:  #  orient_buscar es "vert" o "horiz" entonces
               #  es el 3r acierto en el mismo barco y lo voy a sacar de la lista

            fil2, col2 = (disparos_anteriores["tocado"][-2][0], disparos_anteriores["tocado"][-2][1])
            fil3, col3 = (disparos_anteriores["tocado"][-3][0], disparos_anteriores["tocado"][-3][1])
            pbarco = sorted(list((disp_fil, disp_col) , (fil2, col2), (fil3, col3)))

            if orient_buscar == "horiz":
                #tengo que distinguir el barco de 3 del barco de 4 ahora - el mecanismo de valid_barco() no lo puede hacer
                if tablero[pbarco[0][0], pbarco[0][1]-1] == "■" or tablero[pbarco[-1][0], pbarco[-1][1]+1] == "■":
                    busco_fil, busco_col = random.choice([(pbarco[0][0], pbarco[0][1]-1), (pbarco[-1][0], pbarco[-1][1]+1)])
                    es4=True
                    validacion_disparos(disp_fil, disp_col, orient_buscar, tocado, es4)
                else: # fue un barco de 3 - lo hundo
                    hundir(vista_del_tablero, disparos_anteriores, (disp_fil, disp_col) , (fil2, col2), (fil3, col3), orient_buscar)
                    tocado = False
                    orient_buscar = None                   
                    print("---------¡¡¡ BARCO de 3 HUNDIDO !!!---------")
                    print(" >>>>>----Puedo hacer otro disparo----->>>>>")
                    disparar_rand(tablero, vista_del_tablero, disparos_anteriores, orient_buscar, tocado, es4)

            elif orient_buscar == "vert":

                if tablero[pbarco[0][0]-1, pbarco[0][1]] == "■" or tablero[pbarco[-1][0]+1, pbarco[-1][1]] == "■":
                    busco_fil, busco_col = random.choice([(pbarco[0][0]-1, pbarco[0][1]), (pbarco[-1][0]+1, pbarco[-1][1])])
                    es4 = True
                    validacion_disparos(disp_fil, disp_col, orient_buscar, tocado, es4)
                else:
                    hundir(vista_del_tablero, disparos_anteriores, (disp_fil, disp_col) , (fil2, col2), (fil3, col3), orient_buscar)
                    tocado = False
                    orient_buscar = None
                    print("---------¡¡¡ BARCO de 3 HUNDIDO !!!---------")
                    print(" >>>>>----Puedo hacer otro disparo----->>>>>")
                    disparar_rand(tablero, vista_del_tablero, disparos_anteriores, orient_buscar, tocado, es4)  

    def validacion_barco(disp_fil, disp_col, orient_buscar=None, tocado=False, es4=False):

        if tocado == False: # aqui se entra al acertar primer X 
                            
           if ( tablero[disp_fil-1, disp_col] == "■" or tablero[disp_fil+1, disp_col] == "■" or
                tablero[disp_fil, disp_col-1] == "■" or tablero[disp_fil, disp_col+1] == "■" ):

                tocado=True                           
                validacion_disparos(disp_fil, disp_col, orient_buscar, tocado, es4)

           else:
                hundir(vista_del_tablero, disparos_anteriores, (disp_fil, disp_col), orient_buscar)
                tocado = False
                orient_buscar = None
                print("---------¡¡¡ BARCO de 1 HUNDIDO !!!---------")
                print(" >>>>>----Puedo hacer otro disparo----->>>>>")
                disparar_rand(tablero, vista_del_tablero, disparos_anteriores, orient_buscar, tocado, es4)

        elif tocado == True:
                # aqui entra un barco de 3 o 4 con 2 casillas tocadas
                fil2, col2 = (disparos_anteriores["tocado"][-2][0], disparos_anteriores["tocado"][-2][1])

                if ( tablero[disp_fil-1, disp_col] == "■" or tablero[disp_fil+1, disp_col] == "■" or
                        tablero[disp_fil, disp_col-1] == "■" or tablero[disp_fil, disp_col+1] == "■" 
                        or
                        tablero[fil2-1, col2] == "■" or tablero[fil2+1, col2] == "■" or
                        tablero[fil2, col2-1] == "■" or tablero[fil2, col2+1] == "■" ):

                        validacion_disparos(disp_fil, disp_col, orient_buscar, tocado, es4)
                else:
                        hundir(vista_del_tablero, disparos_anteriores, (disp_fil, disp_col), (fil2, col2, orient_buscar))
                        tocado = False
                        orient_buscar = None
                        print("---------¡¡¡ BARCO de 2 HUNDIDO !!!---------")
                        print(" >>>>>----Puedo hacer otro disparo----->>>>>")
                        disparar_rand(tablero, vista_del_tablero, disparos_anteriores, orient_buscar, tocado, es4)
                      
    if tocado == True:
         # tomo el disparo del turno previo en el cual habia fallado pero tocado el barco
        buscar_cerca(disparos_anteriores["tocado"][-1][0], disparos_anteriores["tocado"][-1][1], orient_buscar, tocado, es4)
    else: 
        disp_fil = np.random.randint(1, 11)
        disp_col = np.random.randint(1, 11)
    
    print("==============  disparo NUEVO  ===============\n" \
        "================= ", (disp_fil, disp_col), " =================")
   

    if not ((disp_fil, disp_col) in disparos_anteriores):    
       validacion_disparos(disp_fil, disp_col, orient_buscar, tocado, es4) 

    else: 
        print("Este disparo ya existe - reintento") 
        disparar_rand(tablero, vista_del_tablero, disparos_anteriores, orient_buscar, tocado, es4)













