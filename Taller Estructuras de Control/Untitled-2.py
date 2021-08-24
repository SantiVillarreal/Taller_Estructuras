"""
entrada
sueldo-->int-->s
salidas
nuevo_sueldo-->str-->ns
"""
s=int(input("ingrese su sueldo $"))
if s<900000:
 xs=s+(s*0.15)
else:
 xs=s+(s*0.12)
print("su nuevo sueldo es ")  