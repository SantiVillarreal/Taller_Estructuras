
"""
Entradas:
lista-list-->lista
Salidas
lista-list-->lista
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
def numeros_pares(lista):
  aux = []
  for i in lista:
    if(float(i) % 2 == 0):
      aux.append(i)
  return aux
if __name__ == "__main__":
  nueva = eliminar_un_caracter(lista_numeros, "\n")
  nueva_fin = numeros_pares(nueva)
  print(nueva_fin)