""""""
"""4.Busque e imprima la ciudad de Singapur"""
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  if(a=="Singapur: Singapur\n"):
    break
  lista=[]   
print(a)