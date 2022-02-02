from math import sqrt
def distance_to_line(points):
	ax = points[0]
	ay = points[1]
	bx = points[2]
	by = points[3]
	cx = points[4]
	cy = points[5]
	dx = (ay**2*bx + ax*by**2 - (ax*ay + ay*bx)*by + (ax**2 - 2*ax*bx + bx**2)*cx + (ax*ay - ay*bx - (ax - bx)*by)*cy)/(ax**2 + ay**2 - 2*ax*bx + bx**2 - 2*ay*by + by**2)
	dy = -(ax*ay*bx - ay*bx**2 - (ax**2 - ax*bx)*by - (ax*ay - ay*bx - (ax - bx)*by)*cx - (ay**2 - 2*ay*by + by**2)*cy)/(ax**2 + ay**2 - 2*ax*bx + bx**2 - 2*ay*by + by**2)
	AB = sqrt((ax-bx)**2+(ay-by)**2)
	AD = sqrt((ax-dx)**2+(ay-dy)**2)
	BD = sqrt((dx-bx)**2+(dy-by)**2)
	AC = sqrt((ax-cx)**2+(ay-cy)**2)
	BC = sqrt((cx-bx)**2+(cy-by)**2)
	if max([AD,BD])>AB:
		return min([AC,BC])
	else:
		return sqrt((cx-dx)**2+(cy-dy)**2)

def main():
	ans = []
	for _ in range(int(input())):
		p = []
		p = [float(x) for x in input().split()]
		ans.append(str(distance_to_line(p)))
	print(' '.join(ans))

if __name__ == '__main__':
	main()
	