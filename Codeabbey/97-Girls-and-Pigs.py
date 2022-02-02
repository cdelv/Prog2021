def count_solutions(legs, brests):
	solutions = 0
	for x in range(2,20000,2):
		if x!=4:
			pigs = round((brests-legs)/(x-4))
			girls = round((x*legs-4*brests)/(2*x-8))
			if brests==x*pigs+2*girls and pigs>0 and girls>0:
				solutions+=1
	return solutions

def main():
	ans = []
	for _ in range(int(input())):
		legs, brests = [int(x) for x in input().split()]
		ans.append(str(count_solutions(legs,brests)))
	print(' '.join(ans))


if __name__ == '__main__':
	main()