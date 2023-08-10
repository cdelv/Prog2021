def is_valid_luhn(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10 == 0

def fix_missing_digit(number):
    index = number.index("?")
    number_list = list(number)
    for i in range(10):
        number_list[index] = str(i)
        if is_valid_luhn(''.join(number_list)):
            return ''.join(number_list)

def fix_swap_error(number):
    number_list = list(number)
    for i in range(len(number_list) - 1):
        number_list[i], number_list[i+1] = number_list[i+1], number_list[i]
        if is_valid_luhn(''.join(number_list)):
            return ''.join(number_list)
        number_list[i], number_list[i+1] = number_list[i+1], number_list[i] 

answer = []
for i in range(int(input())):
    number = input()
    if "?" in number:
        answer.append(fix_missing_digit(number))
    else:
        answer.append(fix_swap_error(number))

print(' '.join(answer))
