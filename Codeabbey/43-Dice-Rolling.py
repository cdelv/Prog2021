
ans = []
for roll in range(int(input())):
	roll = float(input())*6
	ans.append(int(roll)+1)

ans = [str(x) for x in ans]
print(' '.join(ans))