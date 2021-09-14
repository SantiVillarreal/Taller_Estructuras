
"""
Entradas:
lista-list-->lista
lista-str-->elemento
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
def posicion_elemento(lista, elemento):
    lista_posiciones = []
    for i in list(range(0, len(lista))):
        if str(lista[i]) == str(elemento):
            lista_posiciones.append(i)
    return lista_posiciones
if __name__ == "__main__":
  nueva = eliminar_un_caracter(lista_frutas, "\n")
print("Ingrese el nombre de una fruta de la lista:")
elemento = input()
posicion = posicion_elemento(nueva, elemento)
print(posicion)