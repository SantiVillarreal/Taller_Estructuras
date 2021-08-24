"""
entradas
edad-->int-->a
hemoglobina-->int-->b
salidas
resultado-->str--c
"""
a = int(input("ingrese su edad en meses "))
b = float(input("Ingrese su nivel de hemoglobina en % "))
if(a >= 0 and a <= 1):
  if(b >= 12 and b <= 26):
    print("negatipo para Anemia")
  else:
    print("positivo para Anemia")
elif(a > 1 and a <= 6):
  if(b >= 10 and b <= 18):
    print("negatipo para Anemia")
  else:
    print("positivo para Anemia")
elif(a > 6 and a <= 12):
  if(b >= 11 and b <= 15):
    print("negatipo para Anemia")
  else:
    print("positivo para Anemia")
elif(a > 12 and a <= 60):
  if(b >= 11.5 and b <= 15):
    print("negatipo para Anemia")
  else:
    print("positivo para Anemia")
elif(a > 60 and a <= 120):
  if(b >= 12.6 and b <= 15.5):
    print("negatipo para Anemia")
  else:
    print("positivo para Anemia")
elif(a > 120 and a <= 180):
  if(b >= 13 and b <= 15.5):
    print("negatipo para Anemia")
  else:
    print("positivo para Anemia")