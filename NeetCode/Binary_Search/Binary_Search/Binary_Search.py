class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def condition(mid):
            if nums[mid] >= target:
                return True
            return False
        left,right = 0,len(nums)
        while left < right:
            mid = left + (right-left)//2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left if len(nums)>left and nums[left] == target else -1
        
