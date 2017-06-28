#Sumatoria 2
#Suma de las columnas de un arreglo o lista.
#Karla Ivonne Serrano Arevalo

def FilasColumnas(f,c):

    
    minimo = min(f,c)

X=[]
suma=[]
for j in range(f):
  X.append([0]*c)
  print "Matriz X"
    
for j in range(f):
  for k in range(c):
    X[j][k] = (raw_input("Muestra la posicion(%d,%d): " %(j+1,k+1)))
print X
