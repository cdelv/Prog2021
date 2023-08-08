def insertionSort(array, shifted):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        shifts = 0      
        while j >= 0 and key < array[j]:
            shifts += 1
            array[j + 1] = array[j]
            j = j - 1
        
        shifted.append(shifts)
        array[j + 1] = key


input()
array = [int(x) for x in input().split()]
shifted = []
insertionSort(array, shifted)

print(' '.join([str(round(x)) for x in shifted]))