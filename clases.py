#QUE FEO SE VE PHYTON PERO AQUÍ ESTÁN LAS CLASES
class Auto:
    def __init__(self, placa,marca, modelo, descripcion, precio):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.descripcion = descripcion
        self.precio = precio
    
    def saludar(self):
        print("Hola, soy un auto")

class Cliente:
    def __init__(self, nombre, correo, nit):
        self.nombre = nombre
        self.correo = correo
        self.nit = nit

class Compra:
    def __init__(self, productos, cliente, id, total):
        self.id = id
        self.cliente = cliente
        self.total = total
        self.productos = productos