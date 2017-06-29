#The Power Sum
#Suma de Potencias.
#Karla Ivonne Serrano Arevalo

from itertools import combinations
import math

x=int(raw_input())
n=int(raw_input())
m=int(math.pow(x,(1/float(n))))


y=0 
p=[a**n for a in range(m+1)]
for b in range(1,len(p)):
  for c in combinations(p,b):
    if sum(c)==x:
      y+=1
    else:
      pass

print y
