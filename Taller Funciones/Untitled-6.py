
"""
Entradas
lista-list-->lista
elemento-->str-->elemento
Salidas
lista-list-->lista
"""
frutas = open('frutas.txt', 'r')
lista_frutas = []
for i in frutas:
  lista_frutas.append(i)
def eliminar_un_caracter(lista, elemento):
  auxilar = []
  for i in lista:
    a = i.replace(elemento, "")
    auxilar.append(a)
  return auxilar
def letra(lista, elemento):
  auxiliar = []
  for x in lista:
    if(x[0] == "P"):
      print(x)
      auxiliar.append(x)
  return auxiliar
if __name__ == "__main__":
  nueva = eliminar_un_caracter(lista_frutas, "\n")
  nueva_fin = letra(nueva, "")
  print(nueva_fin)