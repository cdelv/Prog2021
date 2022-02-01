answer = []
for problem in range(int(input())):
    total = 0
    numbers = input().split()
    for num in numbers:
    	total += int(num)*int(num)
    answer.append(str(total))
print(' '.join(answer))
