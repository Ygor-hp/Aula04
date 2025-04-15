n=int(input("Digite um numero maior que um:"))
if n<1:
    print("vc e burro ou ta dificio.")
else:
   for x in range(1,n+1,1):
        print(x,end="-")
