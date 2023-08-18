import math as m

def transpose_board(board):
    return [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]

def left(board):
    for row in board:
        # Shift non-zero values to the left
        shifted_row = [0] * len(row)
        j = 0
        
        for value in row:
            if value != 0:
                shifted_row[j] = value
                j += 1
        
        # Merge adjacent equal values
        for i in range(len(shifted_row) - 1):
            if shifted_row[i] == shifted_row[i + 1]:
                shifted_row[i] *= 2
                shifted_row[i + 1] = 0
        
        # Shift the merged row again
        merged_row = [0] * len(row)
        j = 0
        
        for value in shifted_row:
            if value != 0:
                merged_row[j] = value
                j += 1
        
        # Update the board row
        row[:] = merged_row
    
    return board

def right(board):
    for row in board:
        # Shift non-zero values to the right
        shifted_row = [0] * len(row)
        j = len(shifted_row) - 1
        
        for value in reversed(row):
            if value != 0:
                shifted_row[j] = value
                j -= 1
        
        # Merge adjacent equal values
        for i in range(len(shifted_row) - 1, 0, -1):
            if shifted_row[i] == shifted_row[i - 1]:
                shifted_row[i] *= 2
                shifted_row[i - 1] = 0
        
        # Shift the merged row again to the right
        merged_row = [0] * len(row)
        j = len(merged_row) - 1
        
        for value in reversed(shifted_row):
            if value != 0:
                merged_row[j] = value
                j -= 1
        
        # Update the board row
        row[:] = merged_row
    
    return board

def up(board):
    transposed_board = transpose_board(board)
    
    for row in transposed_board:
        # Shift non-zero values upwards
        shifted_row = [0] * len(row)
        j = 0
        
        for value in row:
            if value != 0:
                shifted_row[j] = value
                j += 1
        
        # Merge adjacent equal values
        for i in range(len(shifted_row) - 1):
            if shifted_row[i] == shifted_row[i + 1]:
                shifted_row[i] *= 2
                shifted_row[i + 1] = 0
        
        # Shift the merged row again upwards
        merged_row = [0] * len(row)
        j = 0
        
        for value in shifted_row:
            if value != 0:
                merged_row[j] = value
                j += 1
        
        # Update the transposed board row
        row[:] = merged_row
    
    return transpose_board(transposed_board)

def down(board):
    transposed_board = transpose_board(board)
    
    for row in transposed_board:
        # Shift non-zero values downwards
        shifted_row = [0] * len(row)
        j = len(shifted_row) - 1
        
        for value in reversed(row):
            if value != 0:
                shifted_row[j] = value
                j -= 1
        
        # Merge adjacent equal values
        for i in range(len(shifted_row) - 1, 0, -1):
            if shifted_row[i] == shifted_row[i - 1]:
                shifted_row[i] *= 2
                shifted_row[i - 1] = 0
        
        # Shift the merged row again downwards
        merged_row = [0] * len(row)
        j = len(merged_row) - 1
        
        for value in reversed(shifted_row):
            if value != 0:
                merged_row[j] = value
                j -= 1
        
        # Update the transposed board row
        row[:] = merged_row
    
    return transpose_board(transposed_board)

def print_board(board):
    for row in board:
        print(row)

def move(board, instructions):
    if instruction == "U":
        board = up(board)

    if instruction == "D":
        board = down(board)

    if instruction == "L":
        board = left(board)

    if instruction == "R":
        board = right(board)

    return board

def count_board(board):
    count_dict = {}

    for row in board:
        for num in row:
            try:
                count_dict[num] += 1
            except:
                count_dict[num] = 1
                
    Max = max(count_dict.keys())
    
    for i in range(1, int(m.log2(Max)) + 1):
        print(count_dict.get(2**i,0), end=" ")
    print("\n")

board = []

for _ in range(4):
    board.append([int(x) for x in input().split()])

instructions = input().split()

for instruction in instructions:
    board = move(board, instruction)

count_board(board)