import math as m

def count_characters(input_string):
    char_count = {}
    
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count


answer = []
for _ in range(int(input())):
	input_string = input()
	result = count_characters(input_string)
	H = 0
	for char, count in result.items():
		H += count/len(input_string) *- m.log2(count/len(input_string))
	answer.append(H)

print(' '.join([str(x) for x in answer]))
    
