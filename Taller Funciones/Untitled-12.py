
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
def repetir(lista, elemento):
    lista_posiciones = []
    for i in list(range(0, len(lista))):
        if str(lista[i]) == str(elemento):
            lista_posiciones.append(i)
    return len(lista_posiciones)
if __name__ == "__main__":
  nueva = eliminar_un_caracter(lista_numeros, "\n")
  print("Ingresa un numero de la lista de numeros: ")
  elemento = input()
  repite = repetir(nueva, elemento)
  print(repite)