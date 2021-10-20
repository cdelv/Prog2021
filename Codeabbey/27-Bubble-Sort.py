def bubbleSort(amount, numbers):
    sorted = False
    swapCount, passCount = 0,0

    while not sorted:
        sorted = True
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                sorted = False
                swapCount += 1
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
        passCount += 1

    print(str(passCount)+' '+str(swapCount))


bubbleSort(input(),[int(x) for x in input().split()])