"""
entradas
temperatura-->float-->a
Salidas
deporte-->str-->d
"""
a = float(input("Digite su temperatura :"))
if(a > 85):
  print("Natacion")
elif(a > 71 and a <= 85):
  print("Tenis")
elif(a > 32 and a <= 70):
  print("Golf")
elif(a > 10 and a <= 32):
  print("Esqui")
elif(a <= 10):
  print("Marcha")
else:
  print("No se indentifico ningun deporte")