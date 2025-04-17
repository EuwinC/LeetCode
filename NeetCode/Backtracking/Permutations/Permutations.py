class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        def backtracking(arr=[],used=set()):
            if len(nums) == len(arr):
                res.append(arr.copy()) 
                return
            for i in nums:
                if i in used:
                    continue
                used.add(i)
                arr.append(i)
                backtracking(arr,used)
                arr.pop()
                used.remove(i)
        backtracking()
        return res

              
                
