#Ejercicio1
#Karla Ivonne Serrano Arévalo

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

class votantes:
  def  init (self,ine,nombre,lugarVotacion,Mesa):
    self.INE = ine
    self.NombreApellido = nombre
    self.LugarVotacion = LugarVotacion
    self.MesaVotacion = MesaVotacion

    def getIne (self):
        return self.ine
    def getNombre (self):
        return self.nombre
    def getLugar (self):
        return self.lugarVotacion
    def getMesa (self):
        return self.Mesa

class LugaresVotacion:
  def  init (self,codigo,direccion,localidad):
    self.claveDeLista = codigo
    self.direccion = direccion
    self.localidad = localidad

    def getCodigo (self):
        return self.codigo
    def getDireccion (self):
        return self.direccion
    def getLocalidad (self):
        return self.localidad

class Provincia:
  def  init (self,estado,municipio):
    self.claveDeEstado = estado
    self.claveDeMunicipio = municipio

    def getEstado (self):
        return self.estado
    def getMunicipio (self):
        return self.municipio

class ConsultaLugar:
    def init (self):
        self.pila = Stack()

    def buscar (self,INE):
        contador = 0
        temp = self.pila
        while not temp.isEmpty:
            votantes = temp.pop()
            print votantes.getIne()
            if votantes.getIne()== INE:
                contador = contador + 1
        return contador

    def buscar (self,provincia):
        contador = 0
        temp = self.pila
        while not temp.isEmpty:
            Provincia = temp.pop()
            print Provincia.getMunicipio()
            if Provincia.getMunicipio()== provincia:
                contador = contador + 1
        return contador
