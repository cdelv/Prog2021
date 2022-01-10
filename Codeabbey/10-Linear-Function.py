
def find_slope(a, b, c, d):
    return (d - b) / (c - a)

def find_intercept(a, b, m):
    return (b - m * a)

f = input()
answer = []
for i in range(int(f)):
    a, b, c, d = input().split()
    m = int(find_slope(int(a), int(b), int(c), int(d)))
    g = int(find_intercept(int(a), int(b), m))
    answer.append('({0} {1})'.format(m, g))

print(' '.join(answer))