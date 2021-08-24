"""
entradas
#piezas->int->a
costo_piezas->int->b
salidas
inversion->str->c
prestamo->str->d
credito->str->e
intereses->str->f
"""
a=int(input("ingrese el numero de piezas que se deben comprar "))
b=int(input("ingrese el precio de la pieza "))
t=a*b
if t>5000000:
 c=t*0.55
 d=t*0.30
 e=t*0.15
else: 
 c=t*0.70
 d=0 
 e=t*0.30
f=e*0.20
print("la inversion de la emprsa es de: "+str (c))
print("El prestamo del banco es por "+str (d))
print("El credito es de $ "+ str (e))
print("El credito es de $ " + str(e))
print("Los intereses del credito son de $ " + str(f))