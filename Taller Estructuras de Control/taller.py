"""
entrada
inversion-->int-->a
tasa-->int-->b
salida
dinero_final-->str-->fd
"""
entradas =input("ingrese el valor de la inversion y el de la tasa de interes ").split()
(a, b)=entradas
anv=int(a)
b=int(b)
inter=a*b
if inter>100000:
    print("los intereses generados seran de "+str (inter), " , exeden los $100000")
else:
    print("los intereses generados seran de " +str(inter), " , no exeden los $100000")