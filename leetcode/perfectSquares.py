class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i*i for i in range(n) if i*i <= n]
        squares.remove(0)
        
        num_range = [i for i in range(n+1)] 
        
        n = len(squares) #length of rows
        m = len(num_range) #lenght of columns
        
        tracker = [[0 for i in range(m)] for i in range(n)]
        
        #edge case
        if not tracker:
            return 1
        
        for i in range(len(tracker[0])):
            tracker[0][i] = i
        
        for i in range(1,n):
            for j in range(1,m):
                if j < squares[i]:
                    tracker[i][j] = tracker[i-1][j]
                else:
                    tracker[i][j] = min(tracker[i-1][j],(tracker[i][j-squares[i]] + 1) )
                
        return tracker[n-1][m-1]
                
        
        