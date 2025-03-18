class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        nine = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row[i] or  board[i][j] in col[j]  or  board[i][j] in nine[j//3+int(i//3)*3]:
                    return False 
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                nine[int(j/3)+int(i/3)*3].add(board[i][j])
        
        return True
