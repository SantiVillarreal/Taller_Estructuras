
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
def frutas(lista, elemento):
  lista.append(elemento)
  return lista
if __name__ == "__main__":
  nueva = eliminar_un_caracter(lista_frutas, "\n")
  print("Ingrese la nueva fruta: ")
  elemento = input()
  lista_frutas.append(elemento)
  nueva_fruta = frutas(nueva, elemento)
print(nueva_fruta)
print(lista_frutas)
