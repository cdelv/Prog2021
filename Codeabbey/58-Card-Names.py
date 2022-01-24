def main():
	suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
	ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
	input()
	ans = []
	data = [int(x) for x in input().split()]
	for i in data:
		suit_value = int(i/13)
		rank_value = i%13 
		suit = suits[suit_value]
		rank = ranks[rank_value]
		ans.append(rank+'-of-'+suit)

	print(' '.join(ans))


if __name__ == '__main__':
	main()