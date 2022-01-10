a = input()
Sum = []
vowel = ['a','e','i','o','u','y']
count = 0
for i in range(int(a)):
	word = input()
	for i in word:
		if i in vowel:
			count+=1
	Sum.append(str(count))
	count=0

print(' '.join(Sum))