def Rotate_String(amount):
    answer = []
    for string in range(amount):
        data = input().split()
        rotNum,string = int(data[0]),data[1]
        answer.append(string[rotNum:]+string[:rotNum])
    print(' '.join(answer))


Rotate_String(int(input()))