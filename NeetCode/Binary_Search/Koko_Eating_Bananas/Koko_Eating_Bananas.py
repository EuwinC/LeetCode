class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def condition(mid):
            time = 0
            for pile in piles:
                time += math.ceil(pile/mid)
            return time <= h 
            
        left,right = 1,max(piles)
        while left < right:
            mid = left + (right-left)//2
            if condition(mid):
                right = mid
            else:
                left =mid +1
        return left
        
