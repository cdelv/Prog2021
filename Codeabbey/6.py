a = input()
Sum = []
for i in range(int(a)):
    c, b = input().split()
    Sum.append(str(round(float("%.02f" % (float(c) / float(b))))))

print(' '.join(Sum))