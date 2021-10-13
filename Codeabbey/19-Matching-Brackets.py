a = input()
answer = []
for i in range(int(a)):

	raw_data = input()
	data = (''.join([char for char in raw_data if char in('(){}[]<>')]))

	old_data_length = len(data) + 1

	while len(data) < old_data_length:
		old_data_length = len(data)
		data = data.replace('()','').replace('{}','').replace('[]','').replace('<>','')

	if len(data) > 0:
	    answer.append('0')
	else:
	    answer.append('1')

print(' '.join(answer))
