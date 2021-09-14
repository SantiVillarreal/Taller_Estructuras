
"""
Entradas:
lista-->list-->lista
elemento->str-->elemento
Salidas
lista-->lista
"""
frutas = open('frutas.txt', 'r')
lista_frutas = [] 
for i in frutas:
  lista_frutas.append(i)
def eliminar_un_caracter(lista: list, elemento: str):
  auxilar = []
  for i in lista:
    a = i.replace(elemento, "")
    auxilar.append(a)
  return auxilar
if __name__ == "__main__":
  nueva = eliminar_un_caracter(lista_frutas, ("a"))
  print(nueva)