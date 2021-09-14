
"""
Entradas:
lista->list->lista
Salidas
tamaño-->int->tamaño
tipo-->type-->type
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
def informacion_de_lista(lista):
  aux = []
  for i in lista:
    print(len(lista))
    return aux
if __name__ == "__main__":
  nueva = eliminar_un_caracter(lista_frutas, "\n")
  nueva_fin = informacion_de_lista(nueva)
  print(type(nueva_fin))