def search_str(word):
    Word = sorted(word)
    count = 0
    with open('codeabbey.com_data_words.txt', 'r') as file:
        for line in file:
            if Word == sorted(line.strip()):
                count += 1

    return count - 1


result = []
N = int(input())
for _ in range(N):
    word = input()
    result.append(search_str(word))

print(' '.join([str(x) for x in result]))



        