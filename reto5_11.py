print("Bienvenido al sistema de ubicacion para zonas públicas WIFI")
import os
import sys
import math
from typing import Match
import pandas as pd
nombre_usuario=51703
global contraseña
contraseña=30715
coordenadas=[[0,0],[0,0],[0,0]]
zonas=[[-3.777,-70.302,91],[-4.134,-69.983,233],[-4.006,-70.132,149],[-3.846,-70.222,211]]
print(zonas[0][1] and zonas[1][0] and zonas[2][0] > -4.227 and zonas[0][1] and zonas[1][0] and zonas[2][0]< -3.002)
latitudes1=[[coordenadas[0][0]],[coordenadas[1][0]],[coordenadas[2][0]]]
longitudes1=[[coordenadas[0][1]],[coordenadas[1][1]],[coordenadas[2][1]]]
latitudes2=[[zonas[0][0]],[zonas[1][0]],[zonas[2][0]],[zonas[3][0]]] 
longitudes2=[[zonas[0][1]],[zonas[1][1]],[zonas[2][1],zonas[3][1]]]



lugar1=0
lugar2=0
lugar3=0
lugar4=0
mario=0
uactual1=0
uactual2=0
wifi=0
reunion=0
bus=0
url=0
guardado=0


valor1=int(input("Digite nombre de usuario: "))
if nombre_usuario==valor1:
    valor2=int(input("Digite la contraseña: "))
    if valor2==contraseña: 
        num1=703
        num2=5-3+7-5-4 
        captcha=num1+num2
        resultado=int(input("cuanto es la suma de 703 + 0: "))
        if captcha==resultado:
            print("Sesión iniciada")
            
        else:
            print("Error")
            sys.exit(0) 
    else:
        print("Error")
        sys.exit(0) 
else:
    print("Error")
    sys.exit(0) 

if nombre_usuario==valor1 and valor2==contraseña and captcha==resultado:
    print("Sesión iniciada")
    os.system("cls")
    import sys
    import platform
    import os
    import time
    import math
    class Menu:
    


        '''Muestra un menu y responde a elecciones cuando se ejecuta.'''

        def __init__(self):
            self.elecciones={
                "1":self.uno,
                "2":self.dos,
                "3":self.tres,
                "4":self.cuatro,
                "5":self.cinco,
                "6":self.seis,
                "7":self.quit
            }

            self.menu = ["Cambiar contraseña","Ingresar coordenadas actuales","Ubicar zona wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi desde archivo"]
        

        def mostrar_menu(self):
                print("1.",self.menu[0])
                print("2.",self.menu[1])
                print("3.",self.menu[2])
                print("4.",self.menu[3])
                print("5.",self.menu[4])
                print("6. Elegir opción de menú favorita")
                print("7. Cerrar sesión")
                print(contraseña)
                print(coordenadas)
                print(mario)
                print(wifi)
                print(reunion)

        
        

    

        def run(self):
            '''Muestra el menu y responde a las elecciones.'''
            valoress=0
            while True and valoress!=3:
            
                self.mostrar_menu()
                eleccion = input("Elija una opción: ")
                accion = self.elecciones.get(eleccion)
            
            
                if accion:
                    accion()
                else: 
                    print("Error")
                    if valoress<=3:
                            valoress=valoress+1
        def uno(self):
            print("Usted ha elegido la opción 1")
            global contraseña
            contraseña1=int(input("Escriba la contraseña actual:"))
            if contraseña1==contraseña:
                contraseña=int(input("Escriba la contrseña nueva: "))
            else:
                print("Error")
                sys.exit(0)    

        def dos(self):
            global coordenadas

            if coordenadas==[[0,0],[0,0],[0,0]]:
            
                global latitud1

            

                latitud1 = input("latitud 1: ")
                try:
                    latitud1=float(latitud1)
                    if latitud1<-4.227 or latitud1>-3.002:
                        print("Error coordenada")
                        sys.exit(0)

        
                    print (latitud1)
                    print (type(latitud1))
                except ValueError:
                    print("Error")
                    sys.exit(0)





                global longitud1

                longitud1 = input("longitud 1: ")
                try:
                    longitud1=float(longitud1)
                    if longitud1<-70.365 or longitud1>-69.714:
                        print("Error coordenada")
                        sys.exit(0)
                except ValueError:
                    print("Error")
                    sys.exit(0)





                global latitud2
                latitud2 = input("latitud 2: ")
                try:
                    latitud2=float(latitud2)
                    if latitud2<-4.227 or latitud2>-3.002:
                        print("Error coordenada")
                        sys.exit(0)

        
                    print (latitud2)
                    print (type(latitud2))
                except ValueError:
                    print("Error")
                    sys.exit(0)
            





                global longitud2
                longitud2 = input("longitud 2: ")
                try:
                    longitud2=float(longitud2)
                    if longitud2<-70.365 or longitud2>-69.714:
                        print("Error coordenada")
                        sys.exit(0)
                except ValueError:
                    print("Error")
                    sys.exit(0)



        
                global latitud3
            
                latitud3 = input("latitud 3: ")
                try:
                    latitud3=float(latitud3)
                    if latitud3<-4.227 or latitud3>-3.002:
                        print("Error coordenada")
                        sys.exit(0)
                except ValueError:
                    print("Error")
                    sys.exit(0)

            


        
                global longitud3
                longitud3=input("longitud 3: ")
                try:
                    longitud3=float(longitud3)
                    if longitud3<-70.365 or longitud3>-69.714:
                        print("Error coordenada")
                        sys.exit(0)
                except ValueError:
                    print("Error")
                    sys.exit(0)

            
                coordenadas[0][0]=latitud1
                coordenadas[0][1]=longitud1
                coordenadas[1][0]=latitud2
                coordenadas[1][1]=longitud2
                coordenadas[2][0]=latitud3
                coordenadas[2][1]=longitud3
                print(coordenadas)
            else:
                print(f"coordenada[latitud, longitud] 1 :") 
                print (coordenadas[0])
                print("coordenada[latitud, longitud] 2  :")
                print (coordenadas[1])
                print("coordenada[latitud, longitud] 3  :")
                print (coordenadas[2])
                if coordenadas[0][0]>coordenadas[1][0] and coordenadas[0][0]>coordenadas[2][0]:
                    print("La cordenada 1 es la que está más al norte")
                elif coordenadas[1][0]>coordenadas[2][0] and coordenadas[1][0]>coordenadas[0][0]:
                    print("La cordenada 2 es la que está más al norte")
                else: 
                    print("La cordenada 3 es la que está más al norte")

                promco=(coordenadas[0][0]+coordenadas[1][0]+coordenadas[2][0])/3
                promlon=(coordenadas[1][1]+coordenadas[1][0]+coordenadas[2][1])/3
                coordenada_prom=[promco,promlon]
                print(f"La coordenada promedioes:")
                print(coordenada_prom)
                lolj=int(input("Presione 1,2 o 3 para actualisar la respectiva coordenadas\npresione 0 para regresar al menu"))
                
                if lolj==1:
                    latitud1 = input("latitud 1: ")
                    try:
                        latitud1=float(latitud1)
                        if latitud1<-4.227 or latitud1>-3.002:
                            print("Error coordenada")
                            sys.exit(0)

        
                        print (latitud1)
                        print (type(latitud1))
                    except ValueError:
                        print("Error")
                        sys.exit(0)


                    

                    longitud1 = input("longitud 1: ")
                    try:
                        longitud1=float(longitud1)
                        if longitud1<-70.365 or longitud1>-69.714:
                            print("Error coordenada")
                            sys.exit(0)
                    except ValueError:
                        print("Error")
                        sys.exit(0)

                    coordenadas[0][0]=latitud1
                    coordenadas[0][1]=longitud1

                if lolj==2:
                    latitud2 = input("latitud 2: ")
                    try:
                        latitud2=float(latitud2)
                        if latitud2<-4.227 or latitud2>-3.002:
                            print("Error coordenada")
                            sys.exit(0)

        
                        print (latitud2)
                        print (type(latitud2))
                    except ValueError:
                        print("Error")
                        sys.exit(0)
            




    
                    longitud2 = input("longitud 2: ")
                    try:
                        longitud2=float(longitud2)
                        if longitud2<-70.365 or longitud2>-69.714:
                            print("Error coordenada")
                            sys.exit(0)
                    except ValueError:
                        print("Error")
                        sys.exit(0)

                    coordenadas[1][0]=latitud2
                    coordenadas[1][1]=longitud2


                if lolj==3:
            
                    latitud3 = input("latitud 3: ")
                    try:
                        latitud3=float(latitud3)
                        if latitud3<-4.227 or latitud3>-3.002:
                            print("Error coordenada")
                            sys.exit(0)
                    except ValueError:
                        print("Error")
                        sys.exit(0)

            


        
                    longitud3=input("longitud 3: ")
                    try:
                        longitud3=float(longitud3)
                        if longitud3<-70.365 or longitud3>-69.714:
                            print("Error coordenada")
                            sys.exit(0)
                    except ValueError:
                        print("Error")
                        sys.exit(0)
                    coordenadas[2][0]=latitud3
                    coordenadas[2][1]=longitud3

                if lolj==0:
                    self.mostrar_menu()

                if lolj!=1 and lolj!=2 and lolj!=3 and lolj!=0:
                    print("Error actualización")
                    sys.exit(0)

                    


                











            

        def tres(self):
            print("Usted ha elegido la opción 3")
            if coordenadas==[[0,0],[0,0],[0,0]]:
                print("Error sin registro de coordenadas")
                sys.exit(0)
            else:
                print(f"coordenada[latitud, longitud] 1 :") 
                print (coordenadas[0])
                print("coordenada[latitud, longitud] 2  :")
                print (coordenadas[1])
                print("coordenada[latitud, longitud] 3  :")
                print (coordenadas[2])
                ouo=int(input("Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión"))
                global uactual1
                global uactual2
                global uactual3
                global uactual4
                global uactual5
                global uactual6
                global uactual7
                global uactual8
                global uactual9
                global uactual10
                global lugar1 
                global lugar2
                global lugar3
                global lugar3
                global usuarios1
                global usuarios2
                global mario
                global wifi
                global reunion
                global bus 

                if ouo ==1:

                    uactual1=float(coordenadas[0][0])
                    uactual2=float(coordenadas[0][1])
                    uactual3=float(zonas[0][0])
                    uactual4=float(zonas[0][1])
                    uactual5=float(zonas[1][0])
                    uactual6=float(zonas[1][1])
                    uactual7=float(zonas[2][0])
                    uactual8=float(zonas[2][1])
                    uactual9=float(zonas[3][0])
                    uactual10=float(zonas[3][1])
                    lugar1=self.distancialol(uactual1,uactual2,uactual3,uactual4)
                    lugar2=self.distancialol(uactual1,uactual2,uactual5,uactual6)
                    lugar3=self.distancialol(uactual1,uactual2,uactual7,uactual8)
                    lugar4=self.distancialol(uactual1,uactual2,uactual9,uactual10)
                    print(lugar1)


                    if lugar1<lugar3 and lugar2<lugar3 and lugar1<lugar4 and lugar2<lugar4:

                        usuarios1=zonas[0][2]
                        usuarios2=zonas[1][2]
                        if usuarios1<usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[0]
                            cercana2=zonas[1]
                            print(f"La zona wifi 1: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana1
                                late=uactual1-uactual3
                                longe=uactual2-uactual4
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar1,"bus",bus]

                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()


                            if mario == 2:
                                wifi=cercana2
                                late=uactual1-uactual5
                                longe=uactual2-uactual6
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar2,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            
                            
                        if usuarios1>usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[0]
                            cercana2=zonas[1]
                            print(f"La zona wifi 1: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana2
                                late=uactual1-uactual5
                                longe=uactual2-uactual6
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar2,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            
                                

                            if mario == 2:
                                wifi=cercana1
                                late=uactual1-uactual3
                                longe=uactual2-uactual4
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar1,"bus",bus]

                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()

                            

                    if lugar1<lugar4 and lugar3<lugar4 and lugar1<lugar2 and lugar3<lugar2:
                        usuarios1=zonas[0][2]
                        usuarios2=zonas[2][2]
                        if usuarios1<usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[0]
                            cercana2=zonas[2]
                            print(f"La zona wifi 1: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana1
                                late=uactual1-uactual3
                                longe=uactual2-uactual4
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar1,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()


                            if mario == 2:
                                wifi=cercana2
                                late=uactual1-uactual7
                                longe=uactual2-uactual8
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar3,"bus",bus]

                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            
                            
                        if usuarios1>usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[0]
                            cercana2=zonas[2]
                            print(f"La zona wifi 1: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana2
                                late=uactual1-uactual7
                                longe=uactual2-uactual8
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar3,"bus",bus]
                            

                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            

                            if mario == 2:
                                wifi=cercana1
                                late=uactual1-uactual3
                                longe=uactual2-uactual4
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar1,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu() 

                    if lugar2<lugar1 and lugar3<lugar1 and lugar2<lugar4 and lugar3<lugar4:
                        usuarios1=zonas[1][2]
                        usuarios2=zonas[2][2]
                        if usuarios1<usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[1]
                            cercana2=zonas[2]
                            print(f"La zona wifi 1: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana1
                                late=uactual1-uactual5
                                longe=uactual2-uactual6
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar2,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()


                            if mario == 2:
                                wifi=cercana2
                                late=uactual1-uactual7
                                longe=uactual2-uactual8
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar3,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            
                            
                        if usuarios1>usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[1]
                            cercana2=zonas[2]
                            print(f"La zona wifi 1: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana2
                                late=uactual1-uactual7
                                longe=uactual2-uactual8
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar3,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            

                            if mario == 2:
                                wifi=cercana1
                                late=uactual1-uactual5
                                longe=uactual2-uactual6
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar2,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                            
                            

                    if lugar2<lugar1 and lugar4<lugar1 and lugar2<lugar3 and lugar4<lugar3:
                        usuarios1=zonas[1][2]
                        usuarios2=zonas[3][2]
                        if usuarios1<usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[2]
                            cercana2=zonas[3]
                            print(f"La zona wifi 1: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana1
                                late=uactual1-uactual5
                                longe=uactual2-uactual6
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar2,"bus",bus]
                                

                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()


                            if mario == 2:
                                wifi=cercana2
                                late=uactual1-uactual9
                                longe=uactual2-uactual10
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar4,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            
                            
                        if usuarios1>usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[1]
                            cercana2=zonas[3]
                            print(f"La zona wifi 1: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana2
                                late=uactual1-uactual9
                                longe=uactual2-uactual10
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar4,"bus",bus]
                                

                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            

                            if mario == 2:
                                wifi=cercana1
                                late=uactual1-uactual5
                                longe=uactual2-uactual6
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar2,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()

        

                    if lugar3<lugar1 and lugar4<lugar1 and lugar3<lugar2 and lugar4<lugar2:
                        usuarios1=zonas[2][2]
                        usuarios2=zonas[3][2]
                        if usuarios1<usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[2]
                            cercana2=zonas[3]
                            print(f"La zona wifi 1: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana1
                                late=uactual1-uactual7
                                longe=uactual2-uactual8
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar3,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()


                            if mario == 2:
                                wifi=cercana2
                                late=uactual1-uactual9
                                longe=uactual2-uactual10
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar4,"bus",bus]
                                

                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                           
                        
                            
                        if usuarios1>usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[2]
                            cercana2=zonas[3]
                            print(f"La zona wifi 1: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana2
                                late=uactual1-uactual9
                                longe=uactual2-uactual10
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar4,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            
                            if mario == 2:
                                wifi=cercana1
                                late=uactual1-uactual7
                                longe=uactual2-uactual8
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar3,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu() 

                            


                    if lugar1<lugar2 and lugar4<lugar2 and lugar1<lugar3 and lugar4<lugar3:
                        usuarios1=zonas[0][2]
                        usuarios2=zonas[3][2]
                        if usuarios1<usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[0]
                            cercana2=zonas[3]
                            print(f"La zona wifi 1: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana1
                                late=uactual1-uactual3
                                longe=uactual2-uactual4
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar1,"bus",bus]

                                
                                

                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()


                            if mario == 2:
                                wifi=cercana2
                                late=uactual1-uactual9
                                longe=uactual2-uactual10
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar4,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            
                            
                        if usuarios1>usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[0]
                            cercana2=zonas[3]
                            print(f"La zona wifi 1: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana2
                                late=uactual1-uactual9
                                longe=uactual2-uactual10
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar4,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            

                            if mario == 2:
                                wifi=cercana1
                                late=uactual1-uactual3
                                longe=uactual2-uactual4
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar1,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()

    


                    
            


                    


                    

                if ouo==2:
                    uactual1=coordenadas[1][0]
                    uactual2=coordenadas[1][1]
                    uactual3=float(zonas[0][0])
                    uactual4=float(zonas[0][1])
                    uactual5=float(zonas[1][0])
                    uactual6=float(zonas[1][1])
                    uactual7=float(zonas[2][0])
                    uactual8=float(zonas[2][1])
                    uactual9=float(zonas[3][0])
                    uactual10=float(zonas[3][1])
                    lugar1=self.distancialol(uactual1,uactual2,uactual3,uactual4)
                    lugar2=self.distancialol(uactual1,uactual2,uactual5,uactual6)
                    lugar3=self.distancialol(uactual1,uactual2,uactual7,uactual8)
                    lugar4=self.distancialol(uactual1,uactual2,uactual9,uactual10) 

                    if lugar1<lugar3 and lugar2<lugar3 and lugar1<lugar4 and lugar2<lugar4:

                        usuarios1=zonas[0][2]
                        usuarios2=zonas[1][2]
                        if usuarios1<usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[0]
                            cercana2=zonas[1]
                            print(f"La zona wifi 1: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana1
                                late=uactual1-uactual3
                                longe=uactual2-uactual4
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar1,"bus",bus]

                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()


                            if mario == 2:
                                wifi=cercana2
                                late=uactual1-uactual5
                                longe=uactual2-uactual6
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar2,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            
                            
                        if usuarios1>usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[0]
                            cercana2=zonas[1]
                            print(f"La zona wifi 1: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana2
                                late=uactual1-uactual5
                                longe=uactual2-uactual6
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar2,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            
                                

                            if mario == 2:
                                wifi=cercana1
                                late=uactual1-uactual3
                                longe=uactual2-uactual4
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar1,"bus",bus]

                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()

                            

                    if lugar1<lugar4 and lugar3<lugar4 and lugar1<lugar2 and lugar3<lugar2:
                        usuarios1=zonas[0][2]
                        usuarios2=zonas[2][2]
                        if usuarios1<usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[0]
                            cercana2=zonas[2]
                            print(f"La zona wifi 1: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana1
                                late=uactual1-uactual3
                                longe=uactual2-uactual4
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar1,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()


                            if mario == 2:
                                wifi=cercana2
                                late=uactual1-uactual7
                                longe=uactual2-uactual8
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar3,"bus",bus]

                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            
                            
                        if usuarios1>usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[0]
                            cercana2=zonas[2]
                            print(f"La zona wifi 1: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana2
                                late=uactual1-uactual7
                                longe=uactual2-uactual8
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar3,"bus",bus]
                            

                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            

                            if mario == 2:
                                wifi=cercana1
                                late=uactual1-uactual3
                                longe=uactual2-uactual4
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar1,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu() 

                    if lugar2<lugar1 and lugar3<lugar1 and lugar2<lugar4 and lugar3<lugar4:
                        usuarios1=zonas[1][2]
                        usuarios2=zonas[2][2]
                        if usuarios1<usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[1]
                            cercana2=zonas[2]
                            print(f"La zona wifi 1: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana1
                                late=uactual1-uactual5
                                longe=uactual2-uactual6
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar2,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()


                            if mario == 2:
                                wifi=cercana2
                                late=uactual1-uactual7
                                longe=uactual2-uactual8
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar3,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            
                            
                        if usuarios1>usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[1]
                            cercana2=zonas[2]
                            print(f"La zona wifi 1: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana2
                                late=uactual1-uactual7
                                longe=uactual2-uactual8
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar3,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            

                            if mario == 2:
                                wifi=cercana1
                                late=uactual1-uactual5
                                longe=uactual2-uactual6
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar2,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                            
                            

                    if lugar2<lugar1 and lugar4<lugar1 and lugar2<lugar3 and lugar4<lugar3:
                        usuarios1=zonas[1][2]
                        usuarios2=zonas[3][2]
                        if usuarios1<usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[2]
                            cercana2=zonas[3]
                            print(f"La zona wifi 1: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana1
                                late=uactual1-uactual5
                                longe=uactual2-uactual6
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar2,"bus",bus]
                                

                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()


                            if mario == 2:
                                wifi=cercana2
                                late=uactual1-uactual9
                                longe=uactual2-uactual10
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar4,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            
                            
                        if usuarios1>usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[1]
                            cercana2=zonas[3]
                            print(f"La zona wifi 1: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana2
                                late=uactual1-uactual9
                                longe=uactual2-uactual10
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar4,"bus",bus]
                                

                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            

                            if mario == 2:
                                wifi=cercana1
                                late=uactual1-uactual5
                                longe=uactual2-uactual6
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar2,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()

        

                    if lugar3<lugar1 and lugar4<lugar1 and lugar3<lugar2 and lugar4<lugar2:
                        usuarios1=zonas[2][2]
                        usuarios2=zonas[3][2]
                        if usuarios1<usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[2]
                            cercana2=zonas[3]
                            print(f"La zona wifi 1: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana1
                                late=uactual1-uactual7
                                longe=uactual2-uactual8
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar3,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()


                            if mario == 2:
                                wifi=cercana2
                                late=uactual1-uactual9
                                longe=uactual2-uactual10
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar4,"bus",bus]
                                

                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                           
                        
                            
                        if usuarios1>usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[2]
                            cercana2=zonas[3]
                            print(f"La zona wifi 1: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana2
                                late=uactual1-uactual9
                                longe=uactual2-uactual10
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar4,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            
                            if mario == 2:
                                wifi=cercana1
                                late=uactual1-uactual7
                                longe=uactual2-uactual8
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar3,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu() 

                            


                    if lugar1<lugar2 and lugar4<lugar2 and lugar1<lugar3 and lugar4<lugar3:
                        usuarios1=zonas[0][2]
                        usuarios2=zonas[3][2]
                        if usuarios1<usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[0]
                            cercana2=zonas[3]
                            print(f"La zona wifi 1: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana1
                                late=uactual1-uactual3
                                longe=uactual2-uactual4
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar1,"bus",bus]

                                
                                

                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()


                            if mario == 2:
                                wifi=cercana2
                                late=uactual1-uactual9
                                longe=uactual2-uactual10
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar4,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            
                            
                        if usuarios1>usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[0]
                            cercana2=zonas[3]
                            print(f"La zona wifi 1: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana2
                                late=uactual1-uactual9
                                longe=uactual2-uactual10
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar4,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            

                            if mario == 2:
                                wifi=cercana1
                                late=uactual1-uactual3
                                longe=uactual2-uactual4
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar1,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()

    


                    
                    
                    
                if ouo==3:
                    uactual1=coordenadas[2][0]
                    uactual2=coordenadas[2][1]
                    uactual3=float(zonas[0][0])
                    uactual4=float(zonas[0][1])
                    uactual5=float(zonas[1][0])
                    uactual6=float(zonas[1][1])
                    uactual7=float(zonas[2][0])
                    uactual8=float(zonas[2][1])
                    uactual9=float(zonas[3][0])
                    uactual10=float(zonas[3][1])
                    lugar1=self.distancialol(uactual1,uactual2,uactual3,uactual4)
                    lugar2=self.distancialol(uactual1,uactual2,uactual5,uactual6)
                    lugar3=self.distancialol(uactual1,uactual2,uactual7,uactual8)
                    lugar4=self.distancialol(uactual1,uactual2,uactual9,uactual10)


                    if lugar1<lugar3 and lugar2<lugar3 and lugar1<lugar4 and lugar2<lugar4:

                        usuarios1=zonas[0][2]
                        usuarios2=zonas[1][2]
                        if usuarios1<usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[0]
                            cercana2=zonas[1]
                            print(f"La zona wifi 1: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana1
                                late=uactual1-uactual3
                                longe=uactual2-uactual4
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar1,"bus",bus]

                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()


                            if mario == 2:
                                wifi=cercana2
                                late=uactual1-uactual5
                                longe=uactual2-uactual6
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar2,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            
                            
                        if usuarios1>usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[0]
                            cercana2=zonas[1]
                            print(f"La zona wifi 1: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana2
                                late=uactual1-uactual5
                                longe=uactual2-uactual6
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar2,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            
                                

                            if mario == 2:
                                wifi=cercana1
                                late=uactual1-uactual3
                                longe=uactual2-uactual4
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar1,"bus",bus]

                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()

                            

                    if lugar1<lugar4 and lugar3<lugar4 and lugar1<lugar2 and lugar3<lugar2:
                        usuarios1=zonas[0][2]
                        usuarios2=zonas[2][2]
                        if usuarios1<usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[0]
                            cercana2=zonas[2]
                            print(f"La zona wifi 1: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana1
                                late=uactual1-uactual3
                                longe=uactual2-uactual4
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar1,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()


                            if mario == 2:
                                wifi=cercana2
                                late=uactual1-uactual7
                                longe=uactual2-uactual8
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar3,"bus",bus]

                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            
                            
                        if usuarios1>usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[0]
                            cercana2=zonas[2]
                            print(f"La zona wifi 1: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana2
                                late=uactual1-uactual7
                                longe=uactual2-uactual8
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar3,"bus",bus]
                            

                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            

                            if mario == 2:
                                wifi=cercana1
                                late=uactual1-uactual3
                                longe=uactual2-uactual4
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar1,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu() 

                    if lugar2<lugar1 and lugar3<lugar1 and lugar2<lugar4 and lugar3<lugar4:
                        usuarios1=zonas[1][2]
                        usuarios2=zonas[2][2]
                        if usuarios1<usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[1]
                            cercana2=zonas[2]
                            print(f"La zona wifi 1: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana1
                                late=uactual1-uactual5
                                longe=uactual2-uactual6
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar2,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()


                            if mario == 2:
                                wifi=cercana2
                                late=uactual1-uactual7
                                longe=uactual2-uactual8
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar3,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            
                            
                        if usuarios1>usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[1]
                            cercana2=zonas[2]
                            print(f"La zona wifi 1: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana2
                                late=uactual1-uactual7
                                longe=uactual2-uactual8
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar3,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            

                            if mario == 2:
                                wifi=cercana1
                                late=uactual1-uactual5
                                longe=uactual2-uactual6
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar2,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                            
                            

                    if lugar2<lugar1 and lugar4<lugar1 and lugar2<lugar3 and lugar4<lugar3:
                        usuarios1=zonas[1][2]
                        usuarios2=zonas[3][2]
                        if usuarios1<usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[2]
                            cercana2=zonas[3]
                            print(f"La zona wifi 1: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana1
                                late=uactual1-uactual5
                                longe=uactual2-uactual6
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar2,"bus",bus]
                                

                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()


                            if mario == 2:
                                wifi=cercana2
                                late=uactual1-uactual9
                                longe=uactual2-uactual10
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar4,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            
                            
                        if usuarios1>usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[1]
                            cercana2=zonas[3]
                            print(f"La zona wifi 1: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana2
                                late=uactual1-uactual9
                                longe=uactual2-uactual10
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar4,"bus",bus]
                                

                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            

                            if mario == 2:
                                wifi=cercana1
                                late=uactual1-uactual5
                                longe=uactual2-uactual6
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar2,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()

        

                    if lugar3<lugar1 and lugar4<lugar1 and lugar3<lugar2 and lugar4<lugar2:
                        usuarios1=zonas[2][2]
                        usuarios2=zonas[3][2]
                        if usuarios1<usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[2]
                            cercana2=zonas[3]
                            print(f"La zona wifi 1: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana1
                                late=uactual1-uactual7
                                longe=uactual2-uactual8
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar3,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()


                            if mario == 2:
                                wifi=cercana2
                                late=uactual1-uactual9
                                longe=uactual2-uactual10
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar4,"bus",bus]
                                

                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                           
                        
                            
                        if usuarios1>usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[2]
                            cercana2=zonas[3]
                            print(f"La zona wifi 1: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana2
                                late=uactual1-uactual9
                                longe=uactual2-uactual10
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar4,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            
                            if mario == 2:
                                wifi=cercana1
                                late=uactual1-uactual7
                                longe=uactual2-uactual8
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar3,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu() 

                            


                    if lugar1<lugar2 and lugar4<lugar2 and lugar1<lugar3 and lugar4<lugar3:
                        usuarios1=zonas[0][2]
                        usuarios2=zonas[3][2]
                        if usuarios1<usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[0]
                            cercana2=zonas[3]
                            print(f"La zona wifi 1: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana1
                                late=uactual1-uactual3
                                longe=uactual2-uactual4
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar1,"bus",bus]

                                
                                

                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()


                            if mario == 2:
                                wifi=cercana2
                                late=uactual1-uactual9
                                longe=uactual2-uactual10
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar4,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            
                            
                        if usuarios1>usuarios2:
                            print("Zonas wifi cercanas con menos usuarios")
                            cercana1=zonas[0]
                            cercana2=zonas[3]
                            print(f"La zona wifi 1: ubicada en {cercana2} a {lugar2} metros, tiene un promedio {usuarios2} usuarios" )
                            print(f"La zona wifi 2: ubicada en {cercana1} a {lugar1} metros, tiene un promedio {usuarios1} usuarios" )
                            mario=int(input("Elija 1 o 2 para recibir indicaciones de llegada"))
                            if mario!=1 and mario!=2:
                                print("Error zona wifi")
                                sys.exit(0)
                            if mario==1:
                                wifi=cercana2
                                late=uactual1-uactual9
                                longe=uactual2-uactual10
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar2/16.67)
                                moto=float(lugar2/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar4,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()
                                

                            

                            if mario == 2:
                                wifi=cercana1
                                late=uactual1-uactual3
                                longe=uactual2-uactual4
                                if late>0:
                                    horizonte=str("oriente")
                                else:
                                    horizonte=str("occidente")
                                if longe>0:
                                    yello=str("norte")
                                else:
                                    yello=str("sur")

                                print(f"Para llegar a la zona wifi dirigirse primero al {horizonte} y luego hacia el {yello}")
                                bus=float(lugar1/16.67)
                                moto=float(lugar1/19.44)
                                print(f"Tiempo en bus: {bus}")
                                print(f"Tiempo en moto: {moto}")

                                reunion=[lugar1,"bus",bus]


                                salid=int(input("Presione 0 para salir"))
                                if salid == 0:
                                    self.mostrar_menu()

    






                if ouo!=1 and ouo!=2 and ouo!=3:
                    print("Error ubicación")
                    sys.exit(0)

        def distancialol(self,lat1,lon1,lat2,lon2,R=6372.795477598):
            return (2*R*math.asin(math.sqrt(math.sin((lat2-lat1)/2)**2+math.cos(lat1)*math.cos(lat2)*math.sin((lon2-lon1)/2)**2)))
            
            


        def cuatro(self):
            print("Usted ha elegido la opción 4")
            global guardado
            global url
            global informacion
            if coordenadas==[[0,0],[0,0],[0,0]] and mario==0:
                print("Error de alistamiento")
                sys.exit(0)
            
            if coordenadas!=[[0,0],[0,0],[0,0]] and mario!=0:
                informacion={
                    "actual": [uactual1,uactual2],
                    "zonawifi1":wifi,
                    "recorrido":reunion
                }
                

                hielo=int(input("¿Está de acuerdo con la información a exportar? Presione 1 para confirmar, 0 para regresar al menú principal"))

                if hielo==1:
                    df_wifi=pd.DataFrame()
                    df_wifi["actual"]=[uactual1,uactual2,0]
                    df_wifi["zona_wifi"]=wifi
                    df_wifi["recorrido"]=reunion
                    
                    print(df_wifi)

                    df_wifi.to_csv('Acceso_universal.csv',index=False)

                    print("Exportando archivo")
                    sys.exit(0)


                if hielo==0:
                    self.mostrar_menu()








        def cinco(self):
            print("Usted ha elegido la opción 5")
            url='Acceso_universal.csv'
            df=pd.read_csv(url, error_bad_lines=False)
            print(df.info())
            print(df)
            filas=len(df.index)
            print(f'filas: {filas}')
            
            ben=int(input("\nDatos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal"))
            if ben==0:
                self.mostrar_menu()


        def seis(self):
        
            letras=[]
            lista=[]


            for clave, valor in self.elecciones.items():
                letras.append(clave)
                lista.append(valor)
        
        
            n=int(input("Seleccione opción favorita: "))
            if n>=1 and n<=5:
                print("Para confirmar por favor responda: Si me giras pierdo tres unidades por eso debes colocarme siempre de pie, la respuesta es:")
                a = int(input())
                if a == 0:
                    print("Para confirmar por favor responda: Me separaron de mi hermano siamés, antes era un ocho y ahora soy un… la respuesta es" )
                    b= int(input())
                    if b == 3:
            
                        for recorrid in range(n,n+1):
                            for posicio in range ((n+1)-recorrid):
                                if self.menu[posicio]!=n:
                                    temp=self.menu[posicio]
                                    self.menu[posicio]=self.menu[posicio+(n-1)]
                                    self.menu[posicio+(n-1)]=temp
                        
                        for recorrido in range(n,n+1):
                            for posicion in range ((n+1)-recorrido):
                                if lista[posicion]!=n:
                                    temp=lista[posicion]
                                    lista[posicion]=lista[posicion+(n-1)]
                                    lista[posicion+(n-1)]=temp

                                


                                    self.elecciones=dict()
                                    for i in range(len(letras)):
                                        self.elecciones[letras[i]]=lista[i]
                    else:
                        print("Error")
                else:
                    print("Error")
            else:
                print("Error")
                sys.exit(0)     



        def quit(self):
            print("Hasta pronto")
            sys.exit(0)    

        def limpiar_pantalla(): 
            os.system('cls')
                                    

    Menu().run()
    
                
else:
    print("Error")


    



