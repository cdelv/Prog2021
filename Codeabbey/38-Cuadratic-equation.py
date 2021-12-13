import math

def solve(a,b,c):
	Complex = False
	D = b**2-4*a*c
	O = -b/(2*a)
	if D<0:
		D=-D
		Complex = True

	root1 = O+math.sqrt(D)/(2*a)
	root2 = O-math.sqrt(D)/(2*a)

	if Complex:
		root1 = str(int(O))+str('+')+str(int(math.sqrt(D)/(2*a)))+str('i')
		root2 = str(int(O))+str('-')+str(int(math.sqrt(D)/(2*a)))+str('i')
		return sorted([root1,root2])

	return sorted([int(root1),int(root2)], reverse=True)


def main():
	n = input()
	Ans = []
	for i in range(int(n)):
		a, b, c = input().split()
		root1, root2 = solve(float(a),float(b),float(c))
		Ans.append([str(root1), str(root2)])

	p=''
	for j in Ans:
		p+=' '.join(j)+str('; ')

	print(p[:-2])


if __name__ == '__main__':
	main()