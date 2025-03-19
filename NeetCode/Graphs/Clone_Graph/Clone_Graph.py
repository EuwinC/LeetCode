class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        island = 0
        def dfs(i,j):
            if i<0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            if (i,j) in visit:
                return
            if grid[i][j] != "1":
                return
            visit.add((i,j))
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
            
            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i,j) not in visit:
                    dfs(i,j)
                    island +=1
        return island
