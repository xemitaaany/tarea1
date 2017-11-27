#!/usr/bin/python
miarray = ['silvia','federico','miguel','julia','evaristo']
print miarray[2]
for elem in miarray:
  print elem, " es un valor contenido en el array miarray"
for index in range(len(miarray)):
  print miarray[index], " es el valor contenido en el array sub "
index=0
for elem in miarray:
  print index, ":", elem
  index += 1
miarray.append('carlos')
miarray.index('carlos')
'miguel' in miarray
'carlitos' in miarray
