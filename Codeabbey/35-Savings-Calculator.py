def savingsCalc(calculations):
    answer = []
    for calculation in range(calculations):
    
        S, R, P = input().split()
        P = (int(P) / 100.00) + 1
        S,R = int(S),int(R)
        year = 0
        
        while S <= R:
            S *= P
            year += 1

        answer.append(str(year))

    print(' '.join(answer))

savingsCalc(int(input()))