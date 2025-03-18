class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        cur = 0
        last_high = 0
        for i in range(len(height)):
            if last_high > height[i]:
                cur += last_high - height[i]
            else:
                total += cur
                cur = 0
                last_high = height[i]
        cur = 0
        last_high = 0
        height = height[::-1]
        for i in range(len(height)):
            if last_high >= height[i]:
                cur += last_high - height[i]
            else:
                total += cur
                cur = 0
                last_high = height[i]

        return total

