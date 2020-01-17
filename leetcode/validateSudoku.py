def isValidSudoku(board):

    pos = validate_number(board)
    if pos is None:
        return True
    elif pos is not None:
        #check row
        for i in range(len(board[0])):
            num = board[pos[0]]
            if board[pos[0]][i] == num and pos[1] != i:
                return False
        #check column
        for i in range(len(board)):
            num = board[pos[1]]
            if board[i][pos[1]] == num and pos[0] != i:
                return False
        #check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3
        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                num = board[pos[0]][pos[1]]
                if board[i][j] == num and (i,j) != pos:
                    return False
        return True

def validate_number(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != ".":
                return (i,j)
    return None

tester = [[".",".","4",".",".",".","6","3","."],
         [".",".",".",".",".",".",".",".","."],
         ["5",".",".",".",".",".",".","9","."],
         [".",".",".","5","6",".",".",".","."],
         ["4",".","3",".",".",".",".",".","1"],
         [".",".",".","7",".",".",".",".","."],
         [".",".",".","5",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."]]

print(isValidSudoku(tester))