import string
def cleanWord(word):
    word = word.translate(str.maketrans('', '', string.punctuation))
    word = word.lower()
    word = word.replace(' ', '')
    return word

def is_polindrome(word):
	if word == word[::-1]:
	    return 'Y'
	else:
	    return 'N'

def main():
	answer = []
	for _ in range(int(input())):
		word = input()
		word = cleanWord(word)
		answer.append(is_polindrome(word))

	print(' '.join(answer))

if __name__ == '__main__':
	main()