
"""
approach 1: nested for loop
time complexity: O(N^2)
space complexity: O(N)
TLE in LeetCode
"""
class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        non_dup = [] 
        for n in nums: 
            if n in non_dup:
                return True
            else:
                non_dup.append(n)
        return False

"""
approach 2: set
time complexity: O(N)
space complexity: O(N)
"""
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        non_dup = set() # use set but not a array
        for n in nums:
            if n in non_dup:
                return True
            else:
                non_dup.add(n)
        return False

"""
approach 3: Counter
time complexity: O(N)
space complexity: O(N)
"""
class Solution3:
    def containsDuplicate(self, nums: List[int]) -> bool:
        non_dup = collections.Counter(nums) #it is same as a dictionary and it will count how many time it is duplicate in its value
        return False if max(non_dup.values()) == 1 else True
