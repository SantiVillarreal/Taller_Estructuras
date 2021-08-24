"""
Entradas
categoria-->int-->a
salario bruto-->int-->b
"""
a=int(input("Ingrese la categoría"))
b=int(input("Ingrese el salario bruto"))
#caja negra
if (a==1):
    c=("su salario bruto es "+str(b+(b*0.1)))
elif (a==2):
    c= ("Su salario bruto es "+str(b+(b*0.15)))
elif (a==3):
    c= ("Su salario bruto es "+str(b+(b*0.2)))
elif (a==4):
    c= ("Su salario bruto es "+str(b+(b*0.40)))
elif (a==5):
    c= ("Su salario bruto es "+str(b+(b*0.6)))
else:
    c=("Categoria inexistente")
print(c)