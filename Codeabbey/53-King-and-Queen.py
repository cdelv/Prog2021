def look_for_checks(King,Queen):
	rows = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
	distancex = abs(int(King[1])-int(Queen[1]))
	distancey = abs(rows[King[0]]-rows[Queen[0]])
	if King[0]==Queen[0]:
		return 'Y'
	elif King[1]==Queen[1]:
		return 'Y'
	elif distancex==distancey:
		return 'Y'
	else:
		return 'N' 

def main():
	answer = []
	for i in range(int(input())):
		King, Queen = input().split()
		answer.append(look_for_checks(King,Queen))
	print(' '.join(answer))

if __name__ == '__main__':
	main()