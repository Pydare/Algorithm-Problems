
board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
        ]
word = 'FDEC'

def exist(board,word):
    if not board:
        return False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board,i,j,word):
                return True
    return False

def dfs(board,i,j,word):
    if len(word) == 0: #all the characters are checked
        return  True
    if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0] !=board[i][j]:
        return False
    tmp = board[i][j] #first character is found, check the remaining part   
    board[i][j] = '#'

    res = dfs(board, i+1, j, word[1:]) or dfs(board,i-1,j,word[1:]) or dfs(board,i,j+1,word[1:]) or dfs(board,i,j-1,word[1:])
    board[i][j] = tmp
    return res 

ans = exist(board,word)
print(ans) 


#################LEETCODE ARTICLE#########################
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True

        # no match found after all exploration
        return False


    def backtrack(self, row, col, suffix):
        # bottom case: we find match for each letter in the word
        if len(suffix) == 0:
            return True

        # Check the current status, before jumping into backtracking
        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS \
                or self.board[row][col] != suffix[0]:
            return False

        ret = False
        # mark the choice before exploring further.
        self.board[row][col] = '#'
        # explore the 4 neighbor directions
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ret = self.backtrack(row + rowOffset, col + colOffset, suffix[1:])
            # break instead of return directly to do some cleanup afterwards
            if ret: break

        # revert the change, a clean slate and no side-effect
        self.board[row][col] = suffix[0]

        # Tried all directions, and did not find any match
        return ret
