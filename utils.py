import numpy as np
import random



disparos_anteriores = { "agua":set(), "tocado":[] }  # y tambien celdas alrededor de barcos hundidos
flota={ "barco4":[], "barco3":[], "barco2":[], "barco1":[] }


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


def colocar_barcos(tablero, mi_flota):
    if mi_flota[0] == "0":
        mi_flota = ["4", "3", "3", "2", "2", "2", "1", "1", "1", "1"]
        return colocar_barcos_rand(tablero, mi_flota)
    else:
        return colocar_barcos_rand(tablero, mi_flota)


def colocar_barcos_rand(tablero, mi_flota):


    def colocar_barco4_rand(tablero):

        # pin4fil, pin4col - punto 2 del barco [][*][][]
        orient4 =np.random.choice(["vert", "horiz"]) 
    
        if orient4 == "vert":
            pin4fil =np.random.randint(2, tablero.shape[0]-3) # fila de "cabeza" del barco 4
            pin4col =np.random.randint(1, tablero.shape[1]-1) # columna de "cabeza" del barco 4

            choca = np.any(tablero[pin4fil-1:pin4fil+3, pin4col] == "■") or np.any(tablero[pin4fil-1:pin4fil+3, pin4col] == "~")

            if choca == False: 
                tablero[pin4fil-1:pin4fil+3, pin4col]="■" 

                flota["barco4"].append([ (i, pin4col) for i in range(pin4fil-1, pin4fil+3) ])
                
                tablero[pin4fil-2:pin4fil+4, pin4col+1]="~" 
                tablero[pin4fil-2:pin4fil+4, pin4col-1]="~" 
                tablero[pin4fil-2, pin4col]="~" 
                tablero[pin4fil+3, pin4col]="~" 

            else: colocar_barco4_rand(tablero)

        elif orient4 == "horiz": 
            pin4fil =np.random.randint(1, tablero.shape[0]-1)    
            pin4col =np.random.randint(2, tablero.shape[1]-3)   

            choca = np.any(tablero[pin4fil, pin4col-1:pin4col+3] == "■") or np.any(tablero[pin4fil, pin4col-1:pin4col+3] == "~") 

            if choca == False:
                tablero[pin4fil, pin4col-1:pin4col+3]="■"

                flota["barco4"].append([ (pin4fil, i) for i in range(pin4col-1, pin4col+3) ] )
            
                tablero[pin4fil, pin4col-2]="~"
                tablero[pin4fil, pin4col+3]="~"
                tablero[pin4fil+1, pin4col-2:pin4col+4]="~"
                tablero[pin4fil-1, pin4col-2:pin4col+4]="~"
            else: colocar_barco4_rand(tablero)

    def colocar_barco3_rand(tablero):

        # pin3fil, pin3col - punto 2 del barco [][*][]
        orient3 =np.random.choice(["vert", "horiz"]) 
            
        if orient3 == "horiz":

            pin3fil =np.random.randint(1, tablero.shape[0]-1) 
            pin3col =np.random.randint(2, tablero.shape[1]-2)  
            
            choca = np.any(tablero[pin3fil, pin3col-1 : pin3col+2] == "■") or np.any(tablero[pin3fil, pin3col-1 : pin3col+2] == "~")

            if choca == False: 
                tablero[pin3fil, pin3col-1 : pin3col+2] = "■"

                flota["barco3"].append( [ (pin3fil, i) for i in range(pin3col-1, pin3col+2) ] )
              
                tablero[pin3fil, pin3col-2] = "~"
                tablero[pin3fil, pin3col+2] = "~"
                tablero[pin3fil-1, pin3col-2 : pin3col+3] = "~"
                tablero[pin3fil+1, pin3col-2 : pin3col+3] = "~"
            else: colocar_barco3_rand(tablero)

        elif orient3 == "vert":

            pin3fil =np.random.randint(2,tablero.shape[0]-2) 
            pin3col =np.random.randint(1,tablero.shape[1]-1) 
            
            choca = np.any(tablero[pin3fil-1:pin3fil+2, pin3col] == "■") or np.any(tablero[pin3fil-1:pin3fil+2, pin3col] == "~")

            if choca == False: 
                tablero[pin3fil-1:pin3fil+2, pin3col] = "■"
                flota["barco3"].append( [ (i, pin3col) for i in range(pin3fil-1, pin3fil+2) ] )

                tablero[pin3fil-2:pin3fil+3, pin3col-1] = "~"
                tablero[pin3fil-2:pin3fil+3, pin3col+1] = "~"
                tablero[pin3fil-2, pin3col] = "~"
                tablero[pin3fil+2, pin3col] = "~"
            else: colocar_barco3_rand(tablero)

    def colocar_barco2_rand(tablero):
        # pin2fil, pin2col - punto 1 del barco [*][]
        orient2 =np.random.choice(["vert", "horiz"]) 
            
        if orient2 == "horiz":

            pin2fil =np.random.randint(1,tablero.shape[0]-1) 
            pin2col =np.random.randint(1,tablero.shape[1]-2)  
            
            choca = np.any(tablero[pin2fil, pin2col : pin2col+2] == "■") or np.any(tablero[pin2fil, pin2col : pin2col+2] == "~")

            if choca == False: 
                tablero[pin2fil, pin2col : pin2col+2] = "■"
                flota["barco2"].append( [ (pin2fil, i) for i in range(pin2col , pin2col+2) ] )
                
                tablero[pin2fil+1, pin2col-1 : pin2col+3] = "~"
                tablero[pin2fil-1, pin2col-1 : pin2col+3] = "~"
                tablero[pin2fil, pin2col+2] = "~"
                tablero[pin2fil, pin2col-1] = "~"
            else: colocar_barco2_rand(tablero)

        if orient2 == "vert":

            pin2fil =np.random.randint(1,tablero.shape[0]-2) 
            pin2col =np.random.randint(1,tablero.shape[1]-1)  
           
            choca = np.any(tablero[pin2fil : pin2fil+2, pin2col] == "■") or np.any(tablero[pin2fil : pin2fil+2, pin2col] == "~")

            if choca == False: 
                tablero[pin2fil : pin2fil+2, pin2col] = "■"
                flota["barco2"].append( [ (i, pin2col) for i in range(pin2fil , pin2fil+2) ] )

                tablero[pin2fil-1 : pin2fil+3, pin2col+1] = "~"
                tablero[pin2fil-1 : pin2fil+3, pin2col-1] = "~"
                tablero[pin2fil-1, pin2col] = "~"
                tablero[pin2fil+2, pin2col] = "~"
            else: colocar_barco2_rand(tablero)

    def colocar_barco1_rand(tablero):
        
        pin1fil =np.random.randint(1,tablero.shape[0]-1) 
        pin1col =np.random.randint(1,tablero.shape[1]-1)  

        choca = np.any(tablero[pin1fil, pin1col] == "■") or np.any(tablero[pin1fil, pin1col] == "~")

        if choca == False: 
            tablero[pin1fil, pin1col] = "■"
            flota["barco1"].append((pin1fil, pin1col))

            tablero[pin1fil-1, pin1col-1 : pin1col+2] = "~"
            tablero[pin1fil+1, pin1col-1 : pin1col+2] = "~"
            tablero[pin1fil, pin1col-1] = "~"
            tablero[pin1fil, pin1col+1] = "~"
        else: colocar_barco1_rand(tablero)

    for i in mi_flota:
        if i == "4":
            colocar_barco4_rand(tablero)
        elif i == "3":
            colocar_barco3_rand(tablero) 
        elif i == "2":
            colocar_barco2_rand(tablero)
        elif i == "1":
            colocar_barco1_rand(tablero)
        elif i != ("4" or "3" or "2" or "1"):
            pass

    # bordes de tablero bonitos
    tablero[0, :]=np.arange(tablero.shape[1])
    tablero[:, 0]=np.arange(tablero.shape[0])
    tablero[-1, :]=np.full((1,tablero.shape[0]), "1")
    tablero[:, -1]=np.full((1,tablero.shape[1]), "1")


# def disparar(fil, col, tablero, vista_del_tablero=False):
#     fil, col = tuple(input("Mi disparo [fila, columna]: "))


def disparar_rand(tablero, vista_del_tablero):
    
    def hundir(matriz, barco):  # solo para facilitarme los slicings de pads de barcos hundidos
        
        orient=None
        if len(barco) > 1:
            if barco[0][0] == barco[1][0]:
                orient = "horiz"
            elif barco[0][1] == barco[1][1]:
                orient = "vert"

        if orient == "horiz":
            #lista sorteada de casillas del barco
            #max: [(3, 1), (3, 2), (3, 3), (3, 4)]
            # barco=sorted(list(i for i in pos_seq))
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
                
        elif orient == "vert":
            # max: [(1, 2), (2, 2), (3, 2), (4, 2)]
            # barco=sorted(list(i for i in pos_seq))
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
            matriz[barco[0][0]-1, barco[0][1]-1 : barco[0][1] +2] = "~"
            disparos_anteriores["agua"].add((barco[0][0]-1, barco[0][1]-1))
            disparos_anteriores["agua"].add((barco[0][0]-1, barco[0][1]))
            disparos_anteriores["agua"].add((barco[0][0]-1, barco[0][1]+1))
            
            matriz[barco[0][0]+1, barco[0][1]-1 : barco[0][1] +2] = "~"
            disparos_anteriores["agua"].add((barco[0][0]+1, barco[0][1]-1))
            disparos_anteriores["agua"].add((barco[0][0]+1, barco[0][1]))
            disparos_anteriores["agua"].add((barco[0][0]+1, barco[0][1]+1))

            matriz[barco[0][0], barco[0][1]-1] = "~"
            matriz[barco[0][0], barco[0][1]+1] = "~"
            disparos_anteriores["agua"].add((barco[0][0], barco[0][1]-1))
            disparos_anteriores["agua"].add((barco[0][0], barco[0][1]+1))

    def validacion_disparo(disp_fil, disp_col):

        if (disp_fil, disp_col) in flota["barco1"]:
            hundir(vista_del_tablero, [(disp_fil, disp_col)])

            print("---------¡¡¡ BARCO HUNDIDO !!!---------")
            print(" >>>>>----Puedo hacer otro disparo----->>>>>")
            disparar_rand(tablero, vista_del_tablero)

        else:
            barco_list = 0
            for i in flota["barco4"]:
                if (disp_fil, disp_col) in i:
                    barco_list= i
                    break
            for i in flota["barco3"]:
                if (disp_fil, disp_col) in i:
                    barco_list= i
                    break
            for i in flota["barco2"]:
                if (disp_fil, disp_col) in i:
                    barco_list= i
                    break

            counter=len(barco_list)
            for i in barco_list:  # si todavia hay unas celdas vivas - solo disparo
                if tablero[i] == "■":
                    print(" >>>>>----Puedo hacer otro disparo----->>>>>")
                    disparar_rand(tablero, vista_del_tablero)
                    break
                elif tablero[i] == "X": 
                    counter -=1
                    continue
            
            if counter==0:
                hundir(vista_del_tablero, barco_list)
                print("---------¡¡¡ BARCO HUNDIDO !!!---------")
                print(" >>>>>----Puedo hacer otro disparo----->>>>>")
                disparar_rand(tablero, vista_del_tablero)

  
### empieza la funcion
    disp_fil = np.random.randint(1, tablero.shape[0]-1)
    disp_col = np.random.randint(1, tablero.shape[1]-1)

    if not ((disp_fil, disp_col) in disparos_anteriores):    
        print("==============  disparo NUEVO  ===============\n" \
        "================= ", (disp_fil, disp_col), " =================")

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
            validacion_disparo(disp_fil, disp_col)
    
    else: 
        print("Este disparo ya existe - reintento") 
        disparar_rand(tablero, vista_del_tablero)