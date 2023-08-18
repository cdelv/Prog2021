# https://stackoverflow.com/questions/24909612/modified-tower-of-hanoi

N = input()
disks = [int(x) for x in input().split()]

last, t, s = disks[-1], 1, 0
for d in reversed(disks):
    if d < last: t, last = t*2, d
    s = s + t

print(s) 