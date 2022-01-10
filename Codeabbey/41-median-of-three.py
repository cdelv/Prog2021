def findMedian(amount):
        ans = []
        for x in range(int(amount)):
                [a, b, c] = input().split()
                Min = min(int(a), int(b), int(c))
                Max = max(int(a), int(b), int(c))
                for x in [a, b, c]:
                    if int(x) != Min and int(x) != Max:
                        ans.append(str(x))
        print(' '.join(ans))
findMedian(input())