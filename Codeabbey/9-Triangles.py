f = input()
answer = []
for i in range(int(f)):
    a, b, c = input().split()
    if int(a)+int(b) > int(c) and int(a)+int(c) > int(b) and int(b)+int(c)>int(a):
    	answer.append(str(1))
    else:
    	answer.append(str(0))

print(' '.join(answer))