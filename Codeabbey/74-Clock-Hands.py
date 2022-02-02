import math
def position_h(hour, l=6):
	t = hour.split(":")
	h = float(t[0])+float(t[1])/60
	theta = 2*math.pi*(3-h)/12
	x = 10+l*math.cos(theta)
	y = 10+l*math.sin(theta)
	return x, y

def position_m(hour, l=9):
	t = hour.split(":")
	h = float(t[0])*60+float(t[1])
	theta = 2*math.pi*(15-h)/60
	x = 10+l*math.cos(theta)
	y = 10+l*math.sin(theta)
	return x, y

def main():
	input()
	ans = []
	hours = input().split()
	for i in hours:
		xh, yh = position_h(i)
		xm, ym = position_m(i)
		ans.append(str(xh))
		ans.append(str(yh))
		ans.append(str(xm))
		ans.append(str(ym))

	print(' '.join(ans))

if __name__ == '__main__':
	main()