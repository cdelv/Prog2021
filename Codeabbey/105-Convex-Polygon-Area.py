from shapely.geometry import Polygon

def calc_area(points):
	poligon = Polygon(points)
	return poligon.area

def main():
	points = []
	for _ in range(int(input())):
		points.append([int(x) for x in input().split()])
	print(calc_area(points))

if __name__ == '__main__':
	main()