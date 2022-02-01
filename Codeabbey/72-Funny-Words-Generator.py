import sys

def random(N, X0, A=445, C = 700001, M = 2097152):
    n = []
    x_cur = X0
    for x in range(N):
    	x_next = (A * x_cur + C) % M
    	x_cur = x_next
    	n.append(x_cur)
    return n

def main():
	consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','r','s','t','v','w','x','z']
	vowel = ['a','e','i','o','u']

	Nwords, X0 = [900000,99658]
	lengths = 6
	Nletters = lengths*Nwords
	numbers = random(Nletters,X0)

	for i in range(Nwords):
		word = []
		word.append(consonant[numbers[6*i+0]%19])
		word.append(vowel[numbers[6*i+1]%5])
		word.append(consonant[numbers[6*i+2]%19])
		word.append(vowel[numbers[6*i+3]%5])
		word.append(consonant[numbers[6*i+4]%19])
		word.append(vowel[numbers[6*i+5]%5])
		print(''.join(word), end=" ")

if __name__ == '__main__':
	main()