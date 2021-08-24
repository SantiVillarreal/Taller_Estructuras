"""
Entradas
P-->int-->a
Q-->int-->b
"""
a, b=map(int, input("Digite 2 valores:").split())
if a**3+b**4-2*a**2>680:
    print("Los valores "+ str(a)," y ", str(b),"satisfacen la expresion")
else:
    print("Los valores "+ str(a)," y ",str(b),"no satisfacen la expresion")