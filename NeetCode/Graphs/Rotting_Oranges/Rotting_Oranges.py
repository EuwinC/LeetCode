class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW,COL = len(grid), len(grid[0])
        queue = deque()
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    queue.append([i,j])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        time = 0
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr,dc in directions:
                    i,j = dr + r,dc +c
                    if i == ROW or j == COL or i < 0 or j <0 or grid[i][j] != 1:
                        continue
                    grid[i][j] = 2
                    queue.append([i,j])
            time +=1
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    return -1
        return time -1 if time != 0 else 0
