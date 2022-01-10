
def fifth_power_digit_sum(n,powr=5):
	Sum =0
	for i in str(n):
		Sum += int(i)**powr
	return Sum

def main():
	ans = sum(i for i in range(2, 1000000) if i == fifth_power_digit_sum(i))
	print(str(ans))

if __name__ == '__main__':
	main()