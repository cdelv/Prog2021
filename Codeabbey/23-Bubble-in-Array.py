def checkSum(array):
    result = 0
    
    for number in array:
        result += int(number)
        result *= 113
        result %= 10000007
    return result


array = input().split()
array.pop()
swaps=0

for i in range(len(array)-1):
	if array[i]>array[i+1]:
		swaps+=1
		a, b = array[i], array[i+1]
		array[i]= b
		array[i+1]= a

print(str(swaps)+' '+str(checkSum(array)))
