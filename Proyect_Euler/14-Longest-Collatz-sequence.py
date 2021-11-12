#Volver para implementar programacion dinamica, debería reducir el tiempo a 2 segundos
num=10
Dict = {}
#while (num<1000000):
for x in range(1000000): #se demora 2 segundos menos
    pass
    n=num
    terms=1
    while (n>1):
        if n==1:break
        while n%2==0:
            if n==1:break
            n=n//2
            terms+=1
        else:
            if n==1:break
            n=3*n+1
            terms+=1
    Dict [terms] = num
    num+=1
print(Dict[max(Dict)])