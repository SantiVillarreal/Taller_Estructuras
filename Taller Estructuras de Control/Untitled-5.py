""
sueldo=float(input("Digite el sueldo: "))
a=float(input("Ventas echas por departamento 1: "))
b=float(input("Ventas echas por departamento 2: ")) 
c=float(input("Ventas echas por departamento 3: ")) 
vt=a+b+c
x=vt*33/100
if a>x:
    a=sueldo+sueldo*20/100
else:
    b=sueldo
if b>x:
    b=sueldo+sueldo*20/100
else:
    b=sueldo
if c>x:
    c=sueldo+sueldo*20/100
else:
    c=sueldo
print("Los vendedores del departamento 1 recibiran un pago de:", a)
print("Los vendedores del departamento 2 recibiran un pago de:", b)
print("Los vendedores del departamento 3 recibiran un pago de:", c)