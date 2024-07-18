import os
os.system('cls')
def menu(titulo,lista):
    print('========================================')
    print(titulo.upper())
    print('========================================')
    while True:
        i=1
        for elem in lista:
            print(i,'.-',elem)
            i+=1
        print(i,'.- Salir')
        opc=input('Ingrese Opción: ')
        if opc.isdigit():
            opc_int=int(opc)
            if opc_int>=1 and opc_int<=i:
                return opc_int
            else:
                print('Debe Ingresar un Número entre 1 y ',i)
        else:
            print('Ingrese Sólo Números')

opciones=['Asignar Sueldos','Clasificar sueldos','Ver estadisticas','Reporte de sueldos','']
opcion=menu(opciones)

Trabajador=['Juan Perez','María garcía','Carlos lopez','Ana Martinez','Pedro Rodriguez','Laura Hernandez','Miguel sanchez','Isabel Gomez','Francisco Diaz','Elena fernandez']
Sueldo=['300000','500000','1000000','2000000','1750000','2450000', '900000','1800000','1500000','1200000']

def asigna_sueldos():
    Sueldo_str=Sueldo[opc-1]
    for dic in Trabajador :
     if dic.get('Trabajadores')==Sueldo_str:
        total+=int(dic.get('Sueldo'))


def clasificar_sueldos():
    Trabajador=[]
    Sueldo=[]
    for Trabajador in Sueldo:
        print(Trabajador, Sueldo)
        if (Trabajador, Sueldo) and (Trabajador,Sueldo):


#no entiendo pq me sale con la linea roja :(( , lo siento                      
def v_estadisticas():
    lista_sueldos= Sueldo.values()
    Sueldo_alto= max(lista_sueldos)
    Sueldo_bajo= min(lista_sueldos)
    Sueldo_media= statitics.geometric.Mean(lista_sueldos)
    Promedio_sueldos= statitics.Mean(lista_sueldos)
    print('Sueldo más bajo', Sueldo_bajo)
    print('Sueldo más alto', Sueldo_alto)
    print('Promedio de sueldos', Promedio_sueldos )
    print('Media geometrica', Sueldo_media)

def reporte_sueldo():

    descuento_salud= (Sueldo*0.07)
    descuento_AFP= (Sueldo*0.12)
    Sueldo_liquido= (Sueldo - descuento_AFP - descuento_salud)

    print('Nombre Empleados', Trabajador)
    print('Sueldo base', Sueldo)
    print('Descuento Salud', descuento_salud)
    print('Descuento AFP', descuento_AFP)
    print('Sueldo liquido',Sueldo_liquido)

#aquí copie lo de generar el json
def generar_informe(lista_trabajador):
    informe = []
    for Trabajador in lista_trabajador:
        Trabajador = {
             print('Nombre Empleado'): [Trabajador]}
        informe.append(lista_trabajador) 
    ninforme_trabajadores ='informe_trabajadores.csv'
    #with open ('Informe trabajadores', 'w', 'utf-8', newline=) as informe_trabajadores.csv:
       # csv.dump(informe, informe_trabajadores )
   

while True:
    opc=menu('Menu Principal',['Asignar Sueldos','Clasificar sueldos','Ver estadisticas','Reporte de sueldos'])
    if opc==1:
        asignar_sueldos_=asigna_sueldos()
            
    elif opc==2:
        cla_sueldos_=clasificar_sueldos()
        
    elif opc==3:
        Ver_estadisticas= v_estadisticas()

    elif opc==4:
        reporte=reporte_sueldo()
        generar_informe()
        
    elif opc ==5:
        print('Programa finalizado ')
        print('Desarrollado por Monsserratt Ampuero')
        print('Rut 21.116.568-5')
    else:
        print('Ingrese Opción valida')
        break