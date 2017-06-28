#CaesarCipher
#Cifrador del Cesar.
#Karla Ivonne Serrano Arevalo

import sys

n = int(raw_input().strip())
s =raw_input().strip();new_s=[]
k=int(raw_input().strip())

encripta=""
for i in s:
  if i.isalpha():
    if i.islower():
      encripta= encripta+chr(((ord(i)-97+k)%26)+97)
    else:
      encripta= encripta+chr(((ord(i)-65+k)%26)+65)
  else:
    encripta= encripta + i
print encripta


