def lcm(a,b): # Least Common Multiple
        return(a * b / gcd(a, b))
        
def gcd(a,b): # Greatest Common Divisor
        while b:      
                a, b = b, a % b
        return a

def findDivisors(pairs):
        answer = []
        for pair in range(pairs):
                a,b = input().split()
                a,b = int(a), int(b)
                answer.append('('+str(int(gcd(a,b)))+' '+str(int(lcm(a,b)))+')')

        print(' '.join(answer))


findDivisors(int(input()))


