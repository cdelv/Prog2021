import collections
print (' '.join(sorted([x for x, y in collections.Counter(input().split()).items() if y > 1])))