#CamelCase
#Contar las palabras a partir de la regla de camelCase.
#Karla Ivonne Serrano Arevalo

import sys

s = raw_input().strip()
sum=1
def cuenta (s,sum):
    for i in range(len(s)):
        if s[i].isupper()==True:
            sum=sum+1
    print sum
cuenta(s,sum)
