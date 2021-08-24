"""
entradas
nombre-->str-->a
monto de la compra-->float-->b
salidas
monto a pagar-->float-->c
descuento-->float-->d
"""
a=str(input("Digite el nombre del cliente:"))
b=float(input("Digite el monto de la compra:"))

if(b<50000):
    d=0
    c=(b*d)
    d=(b-c)

elif(b<50000 and b<=100000):
    d=0.05
    c=(b*d)
    d=(b-c)

elif(b<100000 and b<=7000000):
    d=0.11
    c=(b*d)
    d=(b-c)

elif(b<700000 and b<=1500000):
    d=1.18
    c=(b*d)
    d=(b*c)
elif(b<1500000):
    d=0.25
    c=(b*d)
    d=(b*c)

print("Nombre del cliente:"+str(a))
print("El monto de la compra es:"+str(b))
print("El monto a pagar es de:"+str(c))
print("El descuento es de:"+str(d))