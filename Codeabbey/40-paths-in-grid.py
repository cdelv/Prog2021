def findSolution(maze):
    rows = len(maze)
    cols = len(maze[0])
    dp = [[0]*(cols) for x in range(rows)]

    #init
    for x in range(cols):
        if(maze[0][x]!=1):
            dp[0][x] = 1
        else:
            break
    for x in range(1, rows):
        if(maze[x][0]!=1):
            dp[x][0] = 1
        else:
            break

    for i in range(1, rows):
        for j in range(1, cols):
            if(maze[i][j]!=1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[rows-1][cols-1]

def get_maze():
    maze = []
    n, m = input().split()
    for i in range(int(n)):
        line = input().split()
        maze.append(line)

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] in ['@', '$', '+']:
                maze[i][j] = 0
            if maze[i][j] in ['X']:
                maze[i][j] = 1

    return maze

if __name__ == "__main__":
    maze = get_maze()
    print(findSolution(maze))