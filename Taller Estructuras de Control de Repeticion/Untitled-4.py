from typing import SupportsComplex

a= 0

for b in range(1,13):
    if(b>=1):

      a=1+(5*b)
    elif(b==13):
        break
    if(a==61):
        print("a12= "+str (a))
        c= (a+6)*6
        print("Suma= " +str(c))