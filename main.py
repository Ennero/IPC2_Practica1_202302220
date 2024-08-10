import clases
#Declarando algunas variables globales
salir=False
autos = []
clientes = []
compras = []
add = 1000

def registrar_auto():#Función para registrar un auto
    placa = input("Ingrese la placa del auto: ")
    marca = input("Ingrese la marca del auto: ")
    modelo = input("Ingrese el modelo del auto: ")
    descripcion = input("Ingrese la descripción del auto: ")
    precio = float(input("Ingrese el precio del auto : "))
    auto = clases.Auto(placa, marca, modelo, descripcion, precio)
    autos.append(auto)
    if(autos[len(autos)-1].placa == placa): #Comprobando que si se haya registrado
        print("Auto con placa: ", autos[len(autos)-1].placa, " registrado exitosamente")

def registrar_cliente():#Función para registrar un cliente
    nombre = input("Ingrese el nombre del cliente: ")
    correo = input("Ingrese el correo del cliente: ")
    nit = (input("Ingrese el NIT del cliente: "))
    cliente = clases.Cliente(nombre, correo, nit)
    clientes.append(cliente)
    if(clientes[len(clientes)-1].nit == nit):#Comprobando que si se haya registrado
        print("Cliente ",clientes[len(clientes)-1].nombre," registrado exitosamente")

def realizar_compra():#Función para realizar una compra
    global add
    for k in range(len(clientes)):
        print("========== CLIENTE #", k+1, " ==========")
        print("Nombre: ", clientes[k].nombre)
        print("Correo: ", clientes[k].correo)
        print("NIT: ", clientes[k].nit)
        print("----------------------")
    nit = input("Ingrese el NIT del cliente: ")
    for i in range(len(clientes)):
        n1=True
        if(clientes[i].nit==nit):
            n1=False
            print("Cliente ", clientes[i].nombre ," encontrado")
            cliente = clientes[i]
            comprando=True
            productos=[]
            while comprando:
                print("----------")
                print("ESCOJA UNA OPCIÓN: ")
                print("#1 Agregar auto")
                print("#2 Terminar y generar factura")
                op=input()#Opción para agregar auto o generar factura
                match op:
                    case "1":
                        print("----- AGREGAR AUTO -----")
                        print("Autos Disponibles: ")
                        for i in range(len(autos)): #Mostrando autos disponibles
                            print("#",i+1," Placa:", autos[i].placa, " Marca:", autos[i].marca, "; Modelo:", autos[i].modelo,"; Descripción:", autos[i].descripcion, "; Precio: Q.", autos[i].precio)
                        placa = input("Ingrese la placa del auto a agregar a la compra: ")
                        v1=False
                        for i in range(len(autos)): #Agregando auto a la compra
                            if(autos[i].placa==placa):
                                auto=autos[i]
                                productos.append(auto)
                                if(productos[len(productos)-1].placa==placa):
                                    print("Auto", productos[len(productos)-1].marca, productos[len(productos)-1].modelo,"agregado a la compra")
                                    v1=False
                            else:
                                v1=True  
                        if(v1):
                            print("Placa ingresada no existente") #Por si no existe
                    case "2":
                        print("----- GENERAR FACTURA -----")
                        if(len(productos)==0): #Comprobando que si haya autos en la compra
                            print("No hay autos en la compra")
                            break
                        else:
                            comprando=False
                            subtotal = sum([producto.precio for producto in productos]) #Calculando el total
                            print("Se pueden asegurar los autos por un 15% adicional a su valor")
                            if(len(productos)>1): #Preguntando si se quiere asegurar un auto o varios
                                op1=input("Ingrese [s] si desea agregar seguro al auto comprado, sino ingrese cualquiera tecla: ")
                            else:
                                op1=input("Ingrese [s] si desea agregar seguro a los autos comprados, sino ingrese cualquiera tecla: ")
                            if(op1=="s" or op1=="S"):
                                subtotal=subtotal+(subtotal*0.15)
                                print("Seguro agregado a la compra")
                            else:
                                print("No se agregó seguro a la compra")
                            add=add+1
                            compra=clases.Compra(productos, cliente,add,subtotal) #Creando la compra
                            compras.append(compra)
                            print("FACTURA GENERADA EXITOSAMENTE")
                            print("Total a pagar: Q.", compras[len(compras)-1].total) #Mostrando el total
                            n1=False
                    case _:
                        print("ERROR, Opción no válida")
    if(n1):
        print("Cliente no encontrado, regresando al menú principal")
    
def generar_reporte():#Función para generar un reporte de compras
    print("----- REPORTE DE COMPRAS -----")
    for i in range(len(compras)):
        print("========== COMPRA #", i+1, " ==========")
        print("INFORMACIÓN DEL CLIENTE")
        print("Nombre: ", compras[i].cliente.nombre)
        print("Correo: ", compras[i].cliente.correo)
        print("NIT: ", compras[i].cliente.nit) 
        print("Autos comprados: ", len(compras[i].productos))
        print()
        print("INFORMACIÓN DE SU COMPRA")
        for j in range(len(compras[j].productos)):
            print("----------------------")
            print("Auto #", j+1)
            print(compras[j].productos[j].marca, compras[j].productos[j].modelo), compras[j].productos[j].placa, compras[j].productos[j].descripcion, "Precio: Q.", compras[j].productos[j].precio
            print("Total: Q.", compras[j].total)
    print("========= FIN DE REPORTE ==========")
    
print("---------- SUPER AUTOS GT ----------")
while not salir:
    print("------------------------------------")
    print("ESCOJA UNA OPCIÓN: ")
    print("#1 Registrar Auto")
    print("#2 Registrar Cliente")
    print("#3 Realizar Compra")
    print("#4 Reporte de Compras")
    print("#5 Datos del estudiante")
    print("#6 Salir")
    opcion = input()
    match opcion:
        case "1":
            print("----- REGISTRO DE AUTOS -----")
            registrar_auto()
        case "2":
            print("----- REGISTRO DE CLIENTES -----")
            registrar_cliente()
        case "3":
            print("----- REALIZAR COMPRA -----")
            realizar_compra()
        case "4":
            print("----- REPORTE DE COMPRAS -----")
            generar_reporte()
        case "5":
            print("----- DATOS DEL ESTUDIANTE -----")
            print("Nombre: Enner Esaí Mendizabal Castro")
            print("Carné: 202302220")
            print("Curso: IPC2")
            print("Sección: C")
        case "6":
            salir=True
            print("Saliendo del programa...")
        case _:
            print("ERROR, Opción no válida")


