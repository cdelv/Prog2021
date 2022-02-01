from math import sqrt

answer = []
for triangle in range(int(input())):
    x1,y1,x2,y2,x3,y3 = [int(x) for x in input().split()]
    a = sqrt((x2 - x1)**2 + (y2-y1)**2)
    b = sqrt((x3 - x1)**2 + (y3-y1)**2)
    c = sqrt((x3 - x2)**2 + (y3-y2)**2)
    s = (a + b + c) / 2 
    area = sqrt(s*((s-a)*(s-b)*(s-c))) # Heron's Formula
    answer.append(str(area))
print(' '.join(answer))
