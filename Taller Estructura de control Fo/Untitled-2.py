""""""
"""2.Imprima todos los paises y capitales, cuyo inicio sea con la letra U"""
lista=[]
pais=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  pais.append(a)
  lista=[]
for i in pais:
  if(i[0]=="U"):
    print(i)
lista2=[]
capital=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  capital.append(a)
  lista=[]
for i in capital:
  if(i[0]=="u"):
    print(i)
