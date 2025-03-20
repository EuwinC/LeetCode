class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def to_t(i,j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]):
                return
            if board[i][j] != "O":
                return
            board[i][j] = "T"
            to_t(i+1,j)
            to_t(i,j+1)
            to_t(i,j-1)
            to_t(i-1,j)
        
        for i in range(len(board)):
            to_t(i,0)
            to_t(i,len(board[0])-1)
        
        for j in range(len(board[0])):
            to_t(0,j)
            to_t(len(board)-1,j)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "T":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
