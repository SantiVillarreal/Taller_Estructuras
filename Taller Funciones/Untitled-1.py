
frutas = open('frutas.txt', 'r')
numeros = open('numeros.txt', 'r')
lista_frutas = []
lista_numeros = []
for i in frutas:
  lista_frutas.append(i)
for i in numeros:
  lista_numeros.append(i)
print(lista_frutas)
print(lista_numeros)