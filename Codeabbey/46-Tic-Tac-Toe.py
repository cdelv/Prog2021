answer = []
wins = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[3,5,7],[1,5,9]]

def check_wins(moves):
	for win in wins:
		check =  all(item in moves for item in win)
		if check:
			break

	return check

def moves_to_win(moves):
	check = True
	C = 0
	N = len(moves)

	while check:
		moves.pop()
		for win in wins:
			check =  all(item in moves for item in win)
			if check:
				C+=1
				break
		
	return N-C
	

def tic_tac_toe(games):
	for _ in range(games):

		moves = [int(x) for x in input().split()]
		X = moves[::2]
		O = moves[1::2]

		Xwins = check_wins(X)
		Owins = check_wins(O)
		Xmoves = moves_to_win(X)
		Omoves = moves_to_win(O)

		#print(Xwins,Owins)
		#print(Xmoves,Omoves)

		if not Xwins and not Owins:
			answer.append(str(0))
		elif Xmoves<=Omoves or (Xmoves==5 and Xwins and not Owins):
			answer.append(str(2*Xmoves-1))
		elif Xmoves>Omoves:
			answer.append(str(2*Omoves))

if __name__ == '__main__':
    tic_tac_toe(int(input()))
    print(' '.join(answer))