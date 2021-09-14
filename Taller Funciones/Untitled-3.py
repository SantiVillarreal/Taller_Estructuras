
"""
Entradas:
lista-list-->lista
Salidas
lista-list-->lista
"""
frutas = open('frutas.txt', 'r')
numeros = open('numeros.txt', 'r')
lista_frutas = []
lista_numeros = []
for i in frutas:
  lista_frutas.append(i)
for i in numeros:
  lista_numeros.append(i)
def copia(lista: list):
  return lista.copy()
if __name__ == "__main__":
  print(copia(lista_numeros))
  print(copia(lista_frutas))