def timeCalc(calculations):
    answer = []
    for calculation in range(calculations):
        solution = 0
        # Day | hour | minute | second
        d1,h1,m1,s1,d2,h2,m2,s2 = [int(x) for x in input().split()]
    
        if s2 >= s1:
            s = s2 - s1
        else:
            m2 -= 1
            s2 += 60
            s = s2 - s1

        if m2 >= m1:
            m = m2 - m1
        else:
            h2 -= 1
            m2 += 60
            m = m2 - m1
        
        if h2 >= h1:
            h = h2 - h1
        else:
            d2 -= 1
            h2 += 24
            h = h2 - h1
        d = d2 - d1      
        answer.append('({0} {1} {2} {3})'.format(d, h, m, s))

    print(' '.join(answer))
timeCalc(int(input()))