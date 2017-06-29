#Clases y Objetos
#Escribir la clase Point con los métodos descritos en HackerRank.
#Karla Ivonne Serrano Arevalo

from math import sqrt

class Point():
	
	def __init__(self,x,y):
        	self.x=x
		self.y=y
	def reset(self):
        	self.x = 0
        	self.y = 0
	def move(self,x,y):
        	self.x+= x
        	self.y+= y
	def Distancia(self,punto):
		Dist=sqrt((punto.x-self.x)**2+(punto.y-self.y)**2)
		return Dist

D=[]

for i in range((int(raw_input())/2)):
	D.append(Point(*map(int,raw_input().split())).Distancia(Point(*map(int,raw_input().split()))))

for i in D:
    print i



