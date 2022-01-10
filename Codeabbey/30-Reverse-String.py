def Reverse_string(data):
	characters = []
	answer = []

	for character in data:
		characters.append(character)

	for i in reversed(characters):
		answer.append(i)

	print(''.join(answer))

Reverse_string(input())
		