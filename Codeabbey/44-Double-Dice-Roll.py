ans = []
for rolls in range(int(input())):
	roll1, roll2 = [int(x) for x in input().split()]
	roll1 = (roll1%6) +1
	roll2 = (roll2%6) +1
	ans.append(roll1+roll2)

ans = [str(x) for x in ans]
print(' '.join(ans))