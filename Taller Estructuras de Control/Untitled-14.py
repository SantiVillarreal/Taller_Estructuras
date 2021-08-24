"""
Entradas
a-->int-->Consumo de luz electrica anterior
b-->int-->Consumo de luz entrica actual
Salidas
d-->int-->Cantidad a pagar
"""
a=int(input("Ingrese el consumo de luz electrica anterior: "))
b=int(input("Ingrese el consumo de luz electrica actual: "))
c=b-a
#caja negra
if (c<=100):
    d=c*4600
elif (c>=101 and c<=300):
    d=c*80000
elif (c>=301 and c<=500):
    d=c*100000
elif (c>=501):
    d=c*120000
print("Debe pagar un total de: ",d)