class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        def dfs(i,j,ocean,prev = 0):
            if i < 0 or j < 0 or i >=len(heights) or j >=len(heights[i]):
                return
            if prev > heights[i][j]:
                return
            if (i,j) in ocean:
                return
            ocean.add((i,j))
            dfs(i+1,j,ocean,heights[i][j])
            dfs(i,j+1,ocean,heights[i][j])
            dfs(i,j-1,ocean,heights[i][j])
            dfs(i-1,j,ocean,heights[i][j])
        for i in range(len(heights)):
            dfs(i,0,pacific)
            dfs(i,len(heights[0])-1,atlantic)
        
        for j in range(len(heights[0])):
            dfs(0,j,pacific)
            dfs(len(heights)-1,j,atlantic)
        
        res = []
        for p in pacific:
            if p in atlantic:
                res.append(list(p))
        return res

