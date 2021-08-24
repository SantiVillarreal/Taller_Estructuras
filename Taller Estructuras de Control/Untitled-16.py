"""
Entradas
a-->int-->a
b-->int-->b
c-->int-->c
Salidas
e-->int-->e
"""
a=int(input("digite el valor de a: "))
b=int(input("digite el valor de b: "))
c=int(input("digite el valor de c: "))
#caja negra
d=b**2-4*a*c
if (d==0):
    e=-b/(2*a)
elif (d>0):
    e="X1= "+str((-b+(b**2-4*a*c)**(1/2))/(2*a))+" y X2= "+str((-b-(b**2-4*a*c)**(1/2))/(2*a))
elif (d<0):
    e="No tiene solución en los reales"
print(e)