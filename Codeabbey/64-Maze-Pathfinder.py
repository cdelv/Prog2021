import copy
import numpy as np

def get_maze(h):
	maze = []
	line = []
	for _ in range(h):
		row = input()
		for i in row:
			line.append(int(i))
		maze.append(line)
		line = []
	return maze

def search(x,y, mazeList, rows, cols):
    # returns True if it has found end of maze
    if mazeList[x][y] == 'F':
        mazeList[x][y] = 'P'
        return True
    elif mazeList[x][y] == 0:
        return False
    elif mazeList[x][y] == 'C':
        return False
    mazeList[x][y] = 'C'
    if (x < rows -1 and search(x+1,y,mazeList, rows, cols)) or (y > 0 and search(x,y-1,mazeList, rows, cols)) or (x > 0 and search(x-1, y,mazeList, rows, cols)) or (y < cols -1 and search(x, y+1,mazeList, rows, cols)):
        mazeList[x][y] = 'P'
        return True
    return False

def solve_maze(mylist,rows,cols, x, y):
	search(x,y,mylist, rows, cols)
	xarr = []
	yarr = []
	for i in range(0,rows):
	    for j in range(0,cols):
	        if mylist[i][j] =='P':
	            xarr.append(i)
	            yarr.append(j)

	maze = [[None]*cols for _ in range(rows)]

	for i in range(0,len(xarr)):
	    maze[xarr[i]][yarr[i]] = "x"
	for i in range(0,rows):
	    for j in range(0,cols):
	        if maze[i][j] != 'x':
	            maze[i][j] = '-'

	return maze

def path_indications(maze,x,y,path):
	if x == len(maze[0])-1 or x<0:
		return 0
	if y == len(maze)-1 or y<0:
		return 0
	if maze[y][x]=='-':
		return 0

	path.append([x,y])
	return path_indications(maze,x+1,y,path) + path_indications(maze,x-1,y,path) + path_indications(maze,x,y+1,path) + path_indications(maze,x,y-1,path)


def main():
	cols, rows = [int(x) for x in input().split()]
	mylist = get_maze(rows)

	mylist[0][0] = 'F'
	mylist1 = copy.deepcopy(mylist)
	mylist2 = copy.deepcopy(mylist)

	maze = solve_maze(mylist,rows,cols,0,cols-1)
	maze1= solve_maze(mylist1,rows,cols,rows-1,0)
	maze2= solve_maze(mylist2,rows,cols,rows-1,cols-1)

	path = []
	path_indications(maze,0,0,path)
	print(path)

if __name__ == '__main__':
	main()
