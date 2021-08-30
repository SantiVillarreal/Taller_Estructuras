from typing import SupportsComplex


sc= 0

for c in range(1,13):
    if(c>=1):

      sc=1+(5*c)
    elif(c==13):
        break
    if(sc==61):
        print("a12= "+str (sc))
        dc= (sc+6)*6
        print("Suma= " +str(dc))