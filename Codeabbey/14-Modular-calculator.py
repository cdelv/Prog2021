def modCalc(num):
        calc = input().split()
        while calc[0] != "%":
                if calc[0] == '+':
                        num += int(calc[1])
                elif calc[0] == '*':
                        num *= int(calc[1])
                calc = input().split()
        num %= int(calc[1]) 
        print(num)

modCalc(int(input()))