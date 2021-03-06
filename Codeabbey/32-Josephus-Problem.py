def solve_Josephus(specifics):
    people = [int(x) for x in range(1,int(specifics[0])+1)]
    killPosition = int(specifics[1])
    positionCounter = 0
    sorted = False

    while not sorted:
        if len(people) == 1:
            print(people[0])
            sorted = True
        for person in people[:]: #Make copy of iterating list
            positionCounter += 1
            if positionCounter == killPosition:
                people.remove(person)
                positionCounter = 0

solve_Josephus(input().split())