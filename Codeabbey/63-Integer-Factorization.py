t = int(input())
for j in range(t):
    n = int(input())
    i = 2
    a = []
    while n > 1: 
        if n % i == 0:
            n = n // i
            a.append(i)
        else :
            i += 1
    for i in range(len(a)-1):
        print(a[i],end='*')
    print(a[len(a)-1],end=' ')