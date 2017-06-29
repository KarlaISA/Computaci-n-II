class Stack:
     def __init__(self):
         self.items = []
     def isEmpty(self):
         return self.items == []
     def push(self, item):
         self.items.append(item)
     def pop(self):
         return self.items.pop()
     def peek(self):
         return self.items[len(self.items)-1]
     def size(self):
         return len(self.items)

class LlamadasRealizadas:
    def init (self,fecha,hora,noTelf,duracion,valor):
        self.fecha = fecha
        self.hora = hora
        self.noTelf = noTelf
        self.duracion = duracion
        self.valor = valor

    def getFecha (self):
        return self.fecha
    def getHora (self):
        return self.hora
    def getNumeroTelf (self):
        return self.noTelf
    def getDuracion (self):
        return self.duracion
    def getValor (self):
        return self.valor

class Llamadasfacturadas:
    def init (tel1,total1,total2):
        self.TelenoDestino = tel1
        self.TotalFacturado = total1
        self.TotalDeLlamadas = total2

    def getTelefono (self):
        return self.tel1
    def getFacturado (self):
        return self.total1
    def getTotalLlamadas (self):
        return self.total2

class FacturaLlamadasPorFecha:
    def init (self):
        self.pila = Stack()

    def buscar (self,fecha):
        contador = 0
        temp = self.pila
        while not temp.isEmpty:
            LlamadasRealizadas = temp.pop()
            print LlamadasRealizadas.getFecha()
            if LlamadasRealizadas.getFecha()== fecha:
                contador = contador + 1
        return contador

    def buscar (self,TelefonoDestino):
        contador = 0
        temp = self.pila
        while not temp.isEmpty:
            Llamadasfacturadas = temp.pop()
            print Llamadasfacturadas.getTelefono()
            if Llamadasfacturadas.getTelefono()== TelefonoDestino:
                contador = contador + 1
        return contador
