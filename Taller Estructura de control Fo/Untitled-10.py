""""""
"""10.El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato"""

lista=[]
for i in archivo:
  lista.append(i)
  a="".join(lista)
  if(a=="Madagascar: rey julien\n"):
    break
lista2=[]
for i in archivo:
  a=i.index(":")
for i in range(0,len(i)):
  lista2.remove("rey julien")
  lista2.insert("Madagascar: Antananarivo")
  print(lista2)