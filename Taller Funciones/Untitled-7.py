
"""
Entradas:
lista->list->lista
Salidas
tamaño-->int->tamaño
"""
numeros = open('numeros.txt', 'r')
lista_numeros = []
for i in numeros:
  lista_numeros.append(i)
def eliminar_un_caracter(lista, elemento):
  auxilar = []
  for i in lista:
    a = i.replace(elemento, "")
    auxilar.append(a)
  return auxilar
def tamaño_lista(lista):
  aux = []
  for i in lista:
    print(len(lista))
    return aux
if __name__ == "__main__":
  nueva = eliminar_un_caracter(lista_numeros, "\n")
  nueva_fin = tamaño_lista(nueva)
  print(nueva_fin)