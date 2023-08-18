import math as m

X = {'A': 1.0, 'B': 0.5, 'C': -0.5, 'D': -1.0, 'E': -0.5, 'F': 0.5}
Y = {'A': 0.0, 'B': m.sqrt(1 - 0.5**2), 'C': m.sqrt(1 - 0.5**2), 'D': 0.0, 'E': -m.sqrt(1 - 0.5**2), 'F': -m.sqrt(1 - 0.5**2)}

Answare = []

for i in range(int(input())):
    x = 0.0
    y = 0.0
    path = input()
    for letter in path:
        x += X[letter]
        y += Y[letter]

    Answare.append(m.sqrt(x*x + y*y))


print(' '.join([str(x) for x in Answare]))