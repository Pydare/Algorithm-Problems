class Board:
    def __init__(self,n):
        self.n = n
        self.board = [[0 for _ in range(self.n)] for _ in range(self.n)]

    def is_safe(self,row,column):
        #checking the rows
        for i in range(self.n):
            if i != row and self.board[row][i] != 0:
                return False

        #checking the columns
        for j in range(self.n):
            if j != column and self.board[j][column] != 0:
                return False

        #checking the negative diagonal
        for i in range(self.n):
            for j in range(i,i+1):
                if i != row and j != column and self.board[row][column] != 0:
                    return False

        #checking the positive diagonal
        for i in range(self.n):
            for j in range((self.n-i-1),(self.n-i-1)+1):
                if i != row and j != column and self.board[row][column] != 0:
                    return False

        #else none of the conditions is satisfied
        return True

    def place(self,row,column):
        self.board[row][column] = "Q"

    def remove(self,row,column):
        self.board[row][column] = "-"

    def display(self):
        print(self.board)


def queens_helper(board,column):
    #base case
    if column >= 7:
        print(board.display())
        return True
    else:
        #place 1 queen in this column
        for row in range(board.n):
            if board.is_safe(row,column):
                #choose
                board.place(row,column)

                #explore
                if queens_helper(board,column+1)
                    return True

                #unchoose
                board.remove(row,column)
        return False 

def solve_queens(board):
    queens_helper(board,0)
    
#creating a board object
board = Board(8)
print(solve_queens(board))      