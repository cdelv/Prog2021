def quicksort(array, left, right, Answare):
    pivot_pos = partition(array, left, right)
    Answare.append(str(left) + '-' + str(right))

    if pivot_pos - left > 1:
        quicksort(array, left, pivot_pos - 1, Answare)

    if right - pivot_pos > 1:
        quicksort(array, pivot_pos + 1, right, Answare)

def partition(array, left, right):
    lt = left
    rt = right
    dir = 'left'  # specifies at which side is currently "empty" space
    pivot = array[left]
    while lt < rt:
        if dir == 'left':
            if array[rt] > pivot:
                rt = rt - 1
            else:
                array[lt] = array[rt]
                lt = lt + 1
                dir = 'right'
        else:
            if array[lt] < pivot:
                lt = lt + 1
            else:
                # Here it should be assignment, not comparison
                array[rt] = array[lt]
                rt = rt - 1
                dir = 'left'

    # Move the pivot to its final sorted position
    array[lt] = pivot
    return lt

# Read input
input()
Answare = []
Array = [int(x) for x in input().split()]
quicksort(Array, 0, len(Array) - 1, Answare)
print(' '.join(Answare))