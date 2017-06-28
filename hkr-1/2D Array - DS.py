#2D Array - DS
#Recorrer el patrón en las casillas del arreglo.
#Karla Ivonne Serrano Arevalo 

import sys

A = []
B = []

for A_i in xrange(6):
    A.append(map(int,raw_input().strip().split(' ')))

for C in xrange((len(A)-2)):
    for D in xrange((len(A[C])-2)):
        B.append(A[C][D:D+3]+[A[C+1][C+1]]+A[C+2][D:D+3])

print sum(max(B,key=lambda x: sum(x)))

