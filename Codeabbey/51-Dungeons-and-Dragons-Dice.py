def mean(data):
	Sum=0
	for i in data:
		Sum+=i
	return Sum/len(data)

def var(data,mean):
	Sum=0
	for i in data:
		Sum+=(i-mean)**2
	return Sum/len(data)

def main():
	#Espected value of a dice toss with k faces is E=(k+1)/2 and Var=(k^2-1)/12
	#Then, as every toss is independant for n dices tosses will be E=n(k+1)/2 and Var=n(k^2-1)/12
	#Solving the system of equations for n and k
	#n=E^2/(E+3Var) and k=(E+6Var)/(E)
	answer = []
	for i in range(3):
		data=[int(x) for x in input().split()]
		data.pop()
		E=mean(data)
		V=var(data,E)
		n=int(round(E*E/(E+3*V)))
		k=int(round((E+6*V)/E))

		answer.append(str(n)+'d'+str(k))
	print(' '.join(answer))

if __name__ == '__main__':
	main()