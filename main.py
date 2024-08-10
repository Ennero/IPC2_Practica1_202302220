import clases
#Declarando algunas variables globales
salir=False
autos = []
clientes = []
compras = []
cuenta = 1000

def registrar_auto():#Función para registrar un auto
    placa = input("Ingrese la placa del auto: ")
    marca = input("Ingrese la marca del auto: ")
    modelo = input("Ingrese el modelo del auto: ")
    descripcion = input("Ingrese la descripción del auto: ")
    precio = float(input("Ingrese el precio del auto :"))
    auto = clases.Auto(placa, marca, modelo, descripcion, precio)
    autos.append(auto)
    if(autos[len(autos)-1].placa == placa): #Comprobando que si se haya registrado
        print("Auto con placa: ", autos[len(autos)-1].placa, " registrado con exitosamente")

def registrar_cliente():#Función para registrar un cliente
    nombre = input("Ingrese el nombre del cliente:")
    correo = input("Ingrese el correo del cliente:")
    nit = int(input("Ingrese el NIT del cliente:"))
    cliente = clases.Cliente(nombre, correo, nit)
    clientes.append(cliente)
    if(clientes[len(clientes)-1].nit == nit):#Comprobando que si se haya registrado
        print(clientes(len[clientes-1]) ," registrado con exitosamente")

def realizar_compra():#Función para realizar una compra
    nit= input("Ingrese el NIT del cliente: ")
    for i in range(len(clientes)):
        if(clientes[i].nit==nit):
            print("Cliente encontrado")
            cliente = clientes[i]
            comprando=True
            productos=[]
            while comprando:
                print("ESCOJA UNA OPCIÓN: ")
                print("#1 Agregar auto")
                print("#2 Terminar y generar factura")
                op=input()
                match op:
                    case "1":
                        print("----- AGREGAR AUTO -----")
                        print("AUTOS DISPONIBLES")
                        for i in range(len(autos)):
                            print("#",i+1, ". ", autos[i].marca, " ", autos[i].modelo, " ", autos[i].placa, " ", autos[i].descripcion, "; Precio: Q.", autos[i].precio)
                        placa = input("Ingrese la placa del auto a agregar a la compra: ")
                        for i in range(len(autos)):
                            if(autos[i].placa==placa):
                                auto=autos[i]
                                productos.append(auto)
                                if(productos[len(productos)-1].placa==placa):
                                    print("Auto agregado a la compra")
                                else:
                                    print("Error al agregar el auto a la compra")
                    case "2":
                        print("----- GENERAR FACTURA -----")
                        comprando=False
                        subtotal=sum(productos.precio) #Sigo probando si es que sirve de verdad -------------------------------------------------------------------------------------------------------------------------
                        print("Es posible agregar seguro a los autos comprados por un 15% adicional su valor")
                        if(len(productos)>1):
                            op1=input("Ingrese [s] si desea agregar seguro al auto comprado, sino ingrese cualquiera tecla: ")
                        else:
                            op1=input("Ingrese [s] si desea agregar seguro a los autos comprados, sino ingrese cualquiera tecla: ")
                        if(op1=="s" or op1=="S"):
                            subtotal=subtotal+(subtotal*0.15)
                            print("Seguro agregado a la compra")
                        else:
                            print("No se agregó seguro a la compra")
                        compra=clases.Compra(productos, cliente,id,subtotal)
                        id+=1
                        compras.append(compra)
                    case _:
                        print("ERROR, Opción no válida")

                        #cREO QUE LO TERMINÉ, PERO NO SABRÉ SI ESTÁ BIEN HASTA QUE TERMINE DE HACER TODO EL PROGRAMA :=)

            break
        else:
            print("Cliente no encontrado, regresndo al menú principal")
            return
    
    


def generar_reporte():#Función para generar un reporte de compras
    print("----- REPORTE DE COMPRAS -----")
    

    
print("---------- Super Autos GT ----------")

while not salir:
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
            print("--- REGISTRO DE CLIENTES ---")
            registrar_cliente()
        case "3":
            print("--- REALIZAR COMPRA ---")

        case "4":
            print("Generando reporte de compras...")

        case "5":
            print("--- DATOS DEL ESTUDIANTE ---")
            print("Nombre: Enner Esaí Mendizabal Castro")
            print("Carné: 202302220")
            print("Curso: IPC2")
            print("Sección: C")
        case "6":
            salir=True
            print("Saliendo del programa...")
        case _:
            print("ERROR, Opción no válida")


