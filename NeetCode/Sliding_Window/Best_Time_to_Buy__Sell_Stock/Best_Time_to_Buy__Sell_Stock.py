class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr,maxx = float("inf"),0
        for p in prices:
            if p < curr:
                curr = p
            maxx = max(p-curr,maxx)
        return maxx  
