dis=0
alc=0
Gas=0
while True:
 

 dt1=int(input())
 if(dt1==1):
     alc= dt1  
 elif(dt1==2):
      Gas=dt1
 elif(dt1==3):
      dis=dt1
 elif(dt1==4):
     break
 
print("MUCHAS GRACIAS")
print("Alcohol: ",(alc)) 
print("Gasolina: ",(Gas)) 
print("Diesel: ",(dis))   
   