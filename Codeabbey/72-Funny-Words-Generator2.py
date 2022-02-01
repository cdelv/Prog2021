def random(N, X0, A=445, C = 700001, M = 2097152):
    n = []
    x_cur = X0
    for x in range(N):
        x_next = (A * x_cur + C) % M
        x_cur = x_next
        n.append(x_cur)
    return n

def main():
    consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','r','s','t','v','w','x','z']
    vowel = ['a','e','i','o','u']

    Nwords, X0 = [int(x) for x in input().split()]
    lengths = [int(x) for x in input().split()]

    Nletters = sum(lengths)
    numbers = random(Nletters,X0)
    words = []

    for i in range(Nwords):
        word = []
        for j in range(lengths[i]):
            if j%2!=0:
                word.append(vowel[numbers[0]%5])
            else:
                word.append(consonant[numbers[0]%19])
            numbers.pop(0)

        words.append(''.join(word))
    print(' '.join(words))

if __name__ == '__main__':
    main()