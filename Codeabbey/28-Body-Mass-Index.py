def BMI(m,h):
	return m/(h*h)


def findBMI(pairs):
        answer = []
        for pair in range(pairs):
                a,b = input().split()
                a,b = int(a), int(b)
                answer.append('('+str(int(gcd(a,b)))+' '+str(int(lcm(a,b)))+')')

        print(' '.join(answer))


findDivisors(int(input()))