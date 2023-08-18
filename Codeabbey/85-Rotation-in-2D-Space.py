import math

def rotate_point(x, y, a):
    a_rad = math.radians(a)
    new_x = x * math.cos(a_rad) - y * math.sin(a_rad)
    new_y = x * math.sin(a_rad) + y * math.cos(a_rad)
    return new_x, new_y

N, A = map(int, input().split())
stars = []
for _ in range(N):
    name, x, y = input().split()
    stars.append((name, int(x), int(y)))

rotated_stars = []
for name, x, y in stars:
    rotated_x, rotated_y = rotate_point(x, y, A)
    rotated_x = round(rotated_x)
    rotated_y = round(rotated_y)
    rotated_stars.append((rotated_y, rotated_x, name))

# Sort the rotated stars first by Y, then by X
rotated_stars.sort()

# Print the names of the sorted stars
sorted_names = [star[2] for star in rotated_stars]
print(' '.join(sorted_names))