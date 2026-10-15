import numpy as np
import random
import re


class player:

    size = int(input("EL TAMANO DEL TABLERO? \n filas x columnas, filas=columnas="))
    flota_input = list(input("Indique los barcos con los cuales se juega esta partida, separando sus esloras por comas (max eslora es 4).\n" \
                    "Ejemplo (la flota clasica):  4, 3, 3, 2, 2, 2, 1, 1, 1, 1 \n" \
                    "Para usar la flota clasica pulse 0 [enter].\n"))
    # disparos_anteriores = { "agua":set(), "tocado":[] }  # y tambien celdas alrededor de barcos hundidos

    def crear_tablero(self, size=10, vista=False):

        tablero=np.full((size+2, size+2), ".")
        tablero[0, :]=np.arange(size+2)
        tablero[:, 0]=np.arange(size+2)
        tablero[-1, :]=np.full((1,size+2), "1")
        tablero[:, -1]=np.full((1,size+2), "1")

        vista_tablero = np.full((size+2, size+2), ".")
        vista_tablero[0, :]=np.arange(size+2)
        vista_tablero[:, 0]=np.arange(size+2)
        vista_tablero[-1, :]=np.full((1,size+2), "1")
        vista_tablero[:, -1]=np.full((1,size+2), "1")

        if vista == False:
            return tablero
        elif vista == True:
            return vista_tablero


    def __init__(self):
        
        self.disparos_anteriores = { "agua":set(), "tocado":[] }  # y tambien celdas alrededor de barcos hundidos
        self.tablero = self.crear_tablero(self.size)
        self.vista_tablero = self.crear_tablero(self.size, vista=True)
        self.flota = {"barco4":[], "barco3":[], "barco2":[], "barco1":[]}
        self.colocar_barcos()


    def colocar_barcos(self):
        
        if self.flota_input[0] == "0":
            self.flota_input = ["4", "3", "3", "2", "2", "2", "1", "1", "1", "1"]
            self.colocar_barcos_rand()
        else:
            self.colocar_barcos_rand()


    def colocar_barcos_rand(self):

        def colocar_barco4_rand():

            # pin4fil, pin4col - punto 2 del barco [][*][][]
            orient4 =np.random.choice(["vert", "horiz"]) 
        
            if orient4 == "vert":
                pin4fil =np.random.randint(2, self.tablero.shape[0]-3) # fila de "cabeza" del barco 4
                pin4col =np.random.randint(1, self.tablero.shape[1]-1) # columna de "cabeza" del barco 4

                choca = np.any(self.tablero[pin4fil-1:pin4fil+3, pin4col] == "■") or np.any(self.tablero[pin4fil-1:pin4fil+3, pin4col] == "~")

                if choca == False: 
                    self.tablero[pin4fil-1:pin4fil+3, pin4col]="■" 

                    self.flota["barco4"].append([ (i, pin4col) for i in range(pin4fil-1, pin4fil+3) ])
                    
                    self.tablero[pin4fil-2:pin4fil+4, pin4col+1]="~" 
                    self.tablero[pin4fil-2:pin4fil+4, pin4col-1]="~" 
                    self.tablero[pin4fil-2, pin4col]="~" 
                    self.tablero[pin4fil+3, pin4col]="~" 

                else: colocar_barco4_rand()

            elif orient4 == "horiz": 
                pin4fil =np.random.randint(1, self.tablero.shape[0]-1)    
                pin4col =np.random.randint(2, self.tablero.shape[1]-3)   

                choca = np.any(self.tablero[pin4fil, pin4col-1:pin4col+3] == "■") or np.any(self.tablero[pin4fil, pin4col-1:pin4col+3] == "~") 

                if choca == False:
                    self.tablero[pin4fil, pin4col-1:pin4col+3]="■"

                    self.flota["barco4"].append([ (pin4fil, i) for i in range(pin4col-1, pin4col+3) ] )
                
                    self.tablero[pin4fil, pin4col-2]="~"
                    self.tablero[pin4fil, pin4col+3]="~"
                    self.tablero[pin4fil+1, pin4col-2:pin4col+4]="~"
                    self.tablero[pin4fil-1, pin4col-2:pin4col+4]="~"
                else: colocar_barco4_rand()

        def colocar_barco3_rand():

            # pin3fil, pin3col - punto 2 del barco [][*][]
            orient3 =np.random.choice(["vert", "horiz"]) 
                
            if orient3 == "horiz":

                pin3fil =np.random.randint(1, self.tablero.shape[0]-1) 
                pin3col =np.random.randint(2, self.tablero.shape[1]-2)  
                
                choca = np.any(self.tablero[pin3fil, pin3col-1 : pin3col+2] == "■") or np.any(self.tablero[pin3fil, pin3col-1 : pin3col+2] == "~")

                if choca == False: 
                    self.tablero[pin3fil, pin3col-1 : pin3col+2] = "■"

                    self.flota["barco3"].append( [ (pin3fil, i) for i in range(pin3col-1, pin3col+2) ] )
                
                    self.tablero[pin3fil, pin3col-2] = "~"
                    self.tablero[pin3fil, pin3col+2] = "~"
                    self.tablero[pin3fil-1, pin3col-2 : pin3col+3] = "~"
                    self.tablero[pin3fil+1, pin3col-2 : pin3col+3] = "~"
                else: colocar_barco3_rand()

            elif orient3 == "vert":

                pin3fil =np.random.randint(2, self.tablero.shape[0]-2) 
                pin3col =np.random.randint(1, self.tablero.shape[1]-1) 
                
                choca = np.any(self.tablero[pin3fil-1:pin3fil+2, pin3col] == "■") or np.any(self.tablero[pin3fil-1:pin3fil+2, pin3col] == "~")

                if choca == False: 
                    self.tablero[pin3fil-1:pin3fil+2, pin3col] = "■"
                    self.flota["barco3"].append( [ (i, pin3col) for i in range(pin3fil-1, pin3fil+2) ] )

                    self.tablero[pin3fil-2:pin3fil+3, pin3col-1] = "~"
                    self.tablero[pin3fil-2:pin3fil+3, pin3col+1] = "~"
                    self.tablero[pin3fil-2, pin3col] = "~"
                    self.tablero[pin3fil+2, pin3col] = "~"
                else: colocar_barco3_rand()

        def colocar_barco2_rand():
            # pin2fil, pin2col - punto 1 del barco [*][]
            orient2 =np.random.choice(["vert", "horiz"]) 
                
            if orient2 == "horiz":

                pin2fil =np.random.randint(1, self.tablero.shape[0]-1) 
                pin2col =np.random.randint(1, self.tablero.shape[1]-2)  
                
                choca = np.any(self.tablero[pin2fil, pin2col : pin2col+2] == "■") or np.any(self.tablero[pin2fil, pin2col : pin2col+2] == "~")

                if choca == False: 
                    self.tablero[pin2fil, pin2col : pin2col+2] = "■"
                    self.flota["barco2"].append( [ (pin2fil, i) for i in range(pin2col , pin2col+2) ] )
                    
                    self.tablero[pin2fil+1, pin2col-1 : pin2col+3] = "~"
                    self.tablero[pin2fil-1, pin2col-1 : pin2col+3] = "~"
                    self.tablero[pin2fil, pin2col+2] = "~"
                    self.tablero[pin2fil, pin2col-1] = "~"
                else: colocar_barco2_rand()

            if orient2 == "vert":

                pin2fil =np.random.randint(1, self.tablero.shape[0]-2) 
                pin2col =np.random.randint(1, self.tablero.shape[1]-1)  
            
                choca = np.any(self.tablero[pin2fil : pin2fil+2, pin2col] == "■") or np.any(self.tablero[pin2fil : pin2fil+2, pin2col] == "~")

                if choca == False: 
                    self.tablero[pin2fil : pin2fil+2, pin2col] = "■"
                    self.flota["barco2"].append( [ (i, pin2col) for i in range(pin2fil , pin2fil+2) ] )

                    self.tablero[pin2fil-1 : pin2fil+3, pin2col+1] = "~"
                    self.tablero[pin2fil-1 : pin2fil+3, pin2col-1] = "~"
                    self.tablero[pin2fil-1, pin2col] = "~"
                    self.tablero[pin2fil+2, pin2col] = "~"
                else: colocar_barco2_rand()

        def colocar_barco1_rand():
            
            pin1fil =np.random.randint(1, self.tablero.shape[0]-1) 
            pin1col =np.random.randint(1, self.tablero.shape[1]-1)  

            choca = np.any(self.tablero[pin1fil, pin1col] == "■") or np.any(self.tablero[pin1fil, pin1col] == "~")

            if choca == False: 
                self.tablero[pin1fil, pin1col] = "■"
                self.flota["barco1"].append((pin1fil, pin1col))

                self.tablero[pin1fil-1, pin1col-1 : pin1col+2] = "~"
                self.tablero[pin1fil+1, pin1col-1 : pin1col+2] = "~"
                self.tablero[pin1fil, pin1col-1] = "~"
                self.tablero[pin1fil, pin1col+1] = "~"
            else: colocar_barco1_rand()

        for i in self.flota_input:
            if i == "4":
                colocar_barco4_rand()
            elif i == "3":
                colocar_barco3_rand() 
            elif i == "2":
                colocar_barco2_rand()
            elif i == "1":
                colocar_barco1_rand()
            elif i != ("4" or "3" or "2" or "1"):
                pass

        # bordes de tablero bonitos
        self.tablero[0, :]=np.arange(self.tablero.shape[1])
        self.tablero[:, 0]=np.arange(self.tablero.shape[0])
        self.tablero[-1, :]=np.full((1, self.tablero.shape[0]), "1")
        self.tablero[:, -1]=np.full((1, self.tablero.shape[1]), "1")


    def disparar(self, enemigo: "player", rand=False):
    
        def hundir( barco):  # solo para facilitarme los slicings de pads ~ de barcos hundidos
            
            orient = None  # solo paso coordenadas, pero la orientacion del tengo que averiguar y guardarla aqui
            if len(barco) > 1:
                if barco[0][0] == barco[1][0]:
                    orient = "horiz"
                elif barco[0][1] == barco[1][1]:
                    orient = "vert"

                if orient == "horiz":
                        #fila arriba:
                    enemigo.vista_tablero[barco[0][0]-1, barco[0][1]-1 : barco[-1][1]+2] = "~" 
                    alrededores=list( (f-1, c) for f,c in barco )
                    self.disparos_anteriores["agua"].update(alrededores) 
                    self.disparos_anteriores["agua"].add((barco[0][0]-1, barco[0][1]-1)) 
                    self.disparos_anteriores["agua"].add((barco[-1][0]-1, barco[-1][1]+1))    
                        #fila abajo:
                    enemigo.vista_tablero[barco[0][0]+1, barco[0][1]-1 : barco[-1][1]+2] = "~"  
                    alrededores=list((f+1, c) for f,c in barco)
                    self.disparos_anteriores["agua"].update(alrededores)
                    self.disparos_anteriores["agua"].add((barco[0][0]+1, barco[0][1]-1)) 
                    self.disparos_anteriores["agua"].add((barco[-1][0]+1, barco[-1][1]+1)) 
                        #casillas de lados 
                    enemigo.vista_tablero[barco[0][0], barco[0][1]-1] = "~"
                    enemigo.vista_tablero[barco[0][0], barco[-1][1]+1] = "~"
                    self.disparos_anteriores["agua"].add((barco[0][0], barco[0][1]-1))
                    self.disparos_anteriores["agua"].add((barco[0][0], barco[-1][1]+1))
                        
                elif orient == "vert":
                        #columna izq:
                    enemigo.vista_tablero[barco[0][0]-1 : barco[-1][0]+2, barco[0][1]-1 ] = "~" 
                    alrededores=list( (f, c-1) for f,c in barco )
                    self.disparos_anteriores["agua"].update(alrededores) 
                    self.disparos_anteriores["agua"].add((barco[0][0]-1, barco[0][1]-1)) 
                    self.disparos_anteriores["agua"].add((barco[-1][0]+1, barco[-1][1]-1))    
                        #columna der:
                    enemigo.vista_tablero[barco[0][0]-1 : barco[-1][0]+2, barco[0][1]+1] = "~"  
                    alrededores=list((f, c+1) for f,c in barco)
                    self.disparos_anteriores["agua"].update(alrededores)
                    self.disparos_anteriores["agua"].add((barco[0][0]-1, barco[0][1]+1)) 
                    self.disparos_anteriores["agua"].add((barco[-1][0]+1, barco[-1][1]+1)) 
                        #casillas de puntas 
                    enemigo.vista_tablero[barco[0][0]-1, barco[0][1]] = "~"
                    enemigo.vista_tablero[barco[-1][0]+1, barco[-1][1]] = "~"
                    self.disparos_anteriores["agua"].add((barco[0][0]-1, barco[0][1]))
                    self.disparos_anteriores["agua"].add((barco[-1][0]+1, barco[-1][1]))
                
            else:
                # entonces fue un barco de 1: (pos_seq[0][0], pos_seq[0][1])
                enemigo.vista_tablero[barco[0][0]-1, barco[0][1]-1 : barco[0][1] +2] = "~"
                self.disparos_anteriores["agua"].add((barco[0][0]-1, barco[0][1]-1))
                self.disparos_anteriores["agua"].add((barco[0][0]-1, barco[0][1]))
                self.disparos_anteriores["agua"].add((barco[0][0]-1, barco[0][1]+1))
                
                enemigo.vista_tablero[barco[0][0]+1, barco[0][1]-1 : barco[0][1] +2] = "~"
                self.disparos_anteriores["agua"].add((barco[0][0]+1, barco[0][1]-1))
                self.disparos_anteriores["agua"].add((barco[0][0]+1, barco[0][1]))
                self.disparos_anteriores["agua"].add((barco[0][0]+1, barco[0][1]+1))

                enemigo.vista_tablero[barco[0][0], barco[0][1]-1] = "~"
                enemigo.vista_tablero[barco[0][0], barco[0][1]+1] = "~"
                self.disparos_anteriores["agua"].add((barco[0][0], barco[0][1]-1))
                self.disparos_anteriores["agua"].add((barco[0][0], barco[0][1]+1))

        def validacion_disparo(disp_fil, disp_col):

            if (disp_fil, disp_col) in enemigo.flota["barco1"]:
                hundir([(disp_fil, disp_col)])

                print("----------------------------------------------------------¡¡¡ BARCO HUNDIDO !!!------------------")
                print("~~~~~~~~~~~~~~~~______TU tablero______~~~~~~~~~~~~~~~~~_____tablero del ENEMIGO_____~~~~~~~~~~~~~")
                for f1,f2 in zip(self.tablero, enemigo.vista_tablero):
                    print("            ", f1, "               ", f2)

                print(" VVVV---Puedo hacer otro disparo---VVVV----------------------------------------------------------")
                self.disparar(enemigo,  rand)

            else: 
                barco_list = 0  # a esta variable metere la lista de las coordenadas del barco tocado
                for i in enemigo.flota["barco4"]:
                    if (disp_fil, disp_col) in i:
                        barco_list= i
                        break
                for i in enemigo.flota["barco3"]:
                    if (disp_fil, disp_col) in i:
                        barco_list= i
                        break
                for i in enemigo.flota["barco2"]:
                    if (disp_fil, disp_col) in i:
                        barco_list= i
                        break

                counter = len(barco_list)
                for i in barco_list:  # si todavia hay celdas vivas del barco tocado - solo disparo
                    if enemigo.tablero[i] == "■":
                        print("~~~~~~~~~~~~~~~~______TU tablero______~~~~~~~~~~~~~~~~~_____tablero del ENEMIGO_____~~~~~~~~~~~~~")
                        
                        for f1,f2 in zip(self.tablero, enemigo.vista_tablero):
                            print("            ", f1, "               ", f2)

                        print(" VVVV---Puedo hacer otro disparo---VVVV----------------------------------------------------------")
                        self.disparar(enemigo, rand)
                        break
                    elif enemigo.tablero[i] == "X": 
                        counter -=1
                        continue
                
                if counter == 0:
                    hundir(barco_list)
                    print("----------------------------------------------------------¡¡¡ BARCO HUNDIDO !!!------------------")
                    print("~~~~~~~~~~~~~~~~______TU tablero______~~~~~~~~~~~~~~~~~_____tablero del ENEMIGO_____~~~~~~~~~~~~~")
                    
                    for f1,f2 in zip(self.tablero, enemigo.vista_tablero):
                        print("            ", f1, "               ", f2)

                    print(" VVVV---Puedo hacer otro disparo---VVVV----------------------------------------------------------")
                    self.disparar(enemigo,  rand)
    
    ### empieza la funcion
        if rand == True:
                
            disp_fil = np.random.randint(1, enemigo.tablero.shape[0]-1)
            disp_col = np.random.randint(1, enemigo.tablero.shape[1]-1)

        elif rand == False:
            disparo = input("TU disparo fila, columna: ")
        
            (fil, col) = re.split(r"[,;.\s]+", disparo)
            disp_fil= int(fil) 
            disp_col = int(col)
        
        if not ((disp_fil, disp_col) in self.disparos_anteriores):    

            if enemigo.tablero[disp_fil, disp_col] == "~":
                enemigo.tablero[disp_fil, disp_col]="A"
                enemigo.vista_tablero[disp_fil, disp_col]="A"
                self.disparos_anteriores["agua"].add((disp_fil, disp_col))
                
            elif enemigo.tablero[disp_fil, disp_col] == ".":
                enemigo.tablero[disp_fil, disp_col]="A"
                enemigo.vista_tablero[disp_fil, disp_col]="A"
                self.disparos_anteriores["agua"].add((disp_fil, disp_col))

            elif enemigo.tablero[disp_fil, disp_col] == "■":
                enemigo.tablero[disp_fil, disp_col]="X"
                enemigo.vista_tablero[disp_fil, disp_col]="X"
                self.disparos_anteriores["tocado"].append((disp_fil, disp_col))
                validacion_disparo(disp_fil, disp_col)
        
        else: 
            print("Este disparo ya existe - reintento") 
            self.disparar(enemigo, rand)