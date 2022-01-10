def game_score(game):
	score = 0
	for i in game:
		P1_wins = ['RS','SP', 'PR']
		P2_wins = ['SR','PS','RP']
		if i[0]==i[1]:
			score+=0
		elif i in P1_wins:
			score+=1
		elif i in P2_wins:
			score-=1
	if score<0:
		return 2
	else:
		return 1


def main():
	answer = []
	for _ in range(int(input())):
		game = input().split()
		answer.append(str(game_score(game)))
	print(' '.join(answer))

if __name__ == '__main__':
	main()