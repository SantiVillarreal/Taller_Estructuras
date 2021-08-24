"""
Entradas
mes-->int-->a
dia-->int-->b
año-->int-->c
Salidas
d-->str-->signo
"""
a=int(input("Ingresa el numero de tu mes de nacimiento: "))
b=int(input("Ingresa tu dia de nacimiento: "))
c=int(input("Ingresa tu año de nacimiento: "))
#caja negra
if ((a==11 and b>=22)or (a==12 and b<=21)):
    d="Sagitario"
elif ((a==12 and b>=22)or (a==1 and b<=20)):
    d="Capricornio"
elif ((a==1 and b>=21)or (a==2 and b<=19)):
    d="Acuario"
elif ((a==2 and b>=20)or (a==3 and b<=19)):
    d="Piscis"
elif ((a==3 and b>=21)or (a==4 and b<=20)):
    d="Aries"
elif ((a==4 and b>=21)or (a==5 and b<=21)):
    d="Tauro"
elif ((a==5 and b>=22)or (a==6 and b<=21)):
    d="Géminis"
elif ((a==6 and b>=22)or (a==7 and b<=22)):
    d="Cáncer"
elif ((a==7 and b>=23)or (a==8 and b<=23)):
    d="Leo"
elif ((a==8 and b>=24)or (a==9 and b<=22)):
    d="Virgo"
elif ((a==9 and b>=23)or (a==10 and b<=22)):
    d="Libra"
elif ((a==10 and b>=23)or (a==11 and b<=21)):
    d="Escorpión"
print("Usted es ",d)
print("Su edad es ",2021-c)