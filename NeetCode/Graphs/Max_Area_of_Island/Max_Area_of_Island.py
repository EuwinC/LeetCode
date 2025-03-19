class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxx = 0
        visit = set()
        def dfs(i,j,area = 0):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return area
            if (i,j) in visit:
                return area
            if grid[i][j] != 1:
                return area
            visit.add((i,j))
            area = 1+ dfs(i+1,j,area)+dfs(i-1,j,area)+dfs(i,j+1,area)+dfs(i,j-1,area)
            return area
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and (i,j) not in visit:
                    maxx = max(maxx,dfs(i,j))
        return maxx
