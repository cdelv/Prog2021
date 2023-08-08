N = int(input())
array = input().split()
array = [int(x) for x in array]
places = []


for i in range(N - 1):
    index = array[:N - i].index(max(array[:N - i]))
    array[index], array[N - i - 1] = array[N - i - 1], array[index]
    places.append(index)
    

print(' '.join([str(x) for x in places]))