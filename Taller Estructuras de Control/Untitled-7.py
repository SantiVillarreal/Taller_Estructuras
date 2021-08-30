punt=input()
pt1, pt2= punt.split()
pt1=float(pt1)
pt2=float(pt2)
while True:
  
    if(pt2!=0 and pt1!=0):
        total=pt1*pt2
        print("{:.0f}".format(total))
        break