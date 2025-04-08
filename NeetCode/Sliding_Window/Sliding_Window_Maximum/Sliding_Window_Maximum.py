class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []
        
        for i in range(len(nums)):
            # Remove elements not within the sliding window
            if queue and queue[0] < i - k + 1:
                queue.popleft()
            
            # Remove elements smaller than the current element
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            
            queue.append(i)
            
            # Append the maximum element of the current window to the result
            if i >= k - 1:
                res.append(nums[queue[0]])
        
        return res
