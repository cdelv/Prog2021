notes = {'C':1,'C#':2,'D':3,'D#':4,'E':5,'F':6,'F#':7,'G':8,'G#':9,'A':10,'A#':11,'B':12}

def tone(note):
	level = int(note[-1])
	pich = note[:-1]
	N = 12*(level-1)+notes[pich]-notes['A']
	return 55*2**(N/12)

def main():
	ans = []
	input()
	note = input().split()
	for i in note:
		ans.append(str(round(tone(i))))
	print(' '.join(ans))

if __name__ == '__main__':
	main()