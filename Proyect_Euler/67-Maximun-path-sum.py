#primero ingresar un numero al azar
#luego el numero de filas
#despues el triangulo


def max_sum(s,n): 
    ans=[0]+[[0]*i for i in range(1,n+1)]
    for j in range(n):
        ans[n][j]=s[n][j]
    for i in range(n-1,0,-1):
        for j in range(i):
            ans[i][j]=max(ans[i+1][j],ans[i+1][j+1])+s[i][j]
    return ans[1][0]


for _ in range(int(input())):
    n=int(input())
    s=[0]+[list(map(int,input().split())) for i in range(n)]
    print(max_sum(s,n))