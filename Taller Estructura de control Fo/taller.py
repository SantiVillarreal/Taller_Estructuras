archivo = open('paises.txt', 'r')

#imprima la posicion de colombia
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(c)
"""
#Imprima todos los paises
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#Imprima todas las Capitales
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""  
#Imprimir todos los paises que inicien con la letra C
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
"""
#imprima todas las capitales que inicien con la leta B
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)  
"""
#Cuente e imprima cuantas ciudades inician con la latra M  
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range (a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
c=0
for i in ciudad:
  if(i[0]=="M"):
    c=c+1
    print(i)
    print(c)
"""
#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
""""
Capitales
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range (a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="U"):
    print(i)
"""
"""
Paises
lista=[]
paises=[]
for p in archivo:
  b=p.index(":")
  for t in range(0,b):
    lista.append(p[t])
  b="".join(lista)
  paises.append(b)
  lista=[]
for p in paises:
  if(p[0]=="U"):
    print(p)
"""
#Cuente e imprima cuantos paises que hay en el archivo
""""
lista=[]
ciudad=[]
c=0
for i in archivo:
  a=i.index(":")
  c=c+1
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  print(c)
  lista=[]
"""
#Busque e imprima la ciudad de Singapur
"""
lista=[]
for i in archivo:
     if (i=="Singapur: Singapur\n"):
      lista.append(i)
     a="".join(lista) 
print(a)
"""
    
#Busque e imprima el pais de Venezuela y su capital
""""
lista=[]
for i in archivo:
  if (i=="Venezuela: Caracas\n"):
    lista.append(i)
    a="".join(lista)
    print(a)
"""
#Cuente e imprima las ciudades que su pais inicie con la letra E
"""
lista=[]
ciudad=[]
c=0
for i in archivo:
  if (i[0]=="E"):
    lista.append(i)
    a="".join(lista)
    lista=[]
    a=i.index(":")
    for r in range (a+2,len(i)):
      ciudad.append(i[r])
    a="".join(ciudad)
    c=c+1
    print(a)
    print(c)
    ciudad=[]
"""

#Buesque e imprima la Capiltal de Colombia
"""
lista=[]
ciudad=[]
for i in archivo:
  if (i=="Colombia: Bogotá\n"):
    lista.append(i)
    a="".join(lista)
    lista=[]
    a=i.index(":")
    for r in range (a+2,len(i)):
      ciudad.append(i[r])
    a="".join(ciudad)
    print(a)
    ciudad=[]
"""
    
#imprima la posicion del pais de Uganda
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Uganda: Kampala\n"):
    break
  lista=[]   
print(c)
"""
#imprima la posicion del pais de Mexico
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="México: Ciudad de México \n"):
    break
  lista=[]   
print(c)
"""

"""
El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato
"""
"""
lista=[]
for i in archivo: 
  lista.append(i)
  a="".join(lista)
  if(a=="Madagascar: rey julien\n"):
    a=int(a)
    a.pop([2,len(i)])
  a="".join(lista)
  print(a)  
  lista=[]
  a=[]
  ...
  🏳️
"""
#Agregue un país que no esté en la lista 
"""
lista=[]
lista.append("Konoha: Naruto \n")
for i in archivo: 
  lista.append(i)
  a=" ".join(lista)
  print(a)
  a=[]
  lista=[]
"""
archivo.close()