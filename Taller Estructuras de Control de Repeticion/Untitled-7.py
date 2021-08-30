p=input()
p1, p2= p.split()
p1=float(p1)
p2=float(p2)
while True:
    if(p2!=0 and p1!=0):
        total=p1*p2
        print("{:.0f}".format(total))
        break