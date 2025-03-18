class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1,nums[0]]
        sufix = [nums[-1]]

        for i in range(1,len(nums)):
            prefix.append(prefix[-1]*nums[i])
            sufix.append(sufix[-1]*nums[~i])
        res = []
        i,j=0,len(sufix)-2
        while j>=0:
            res.append(prefix[i]*sufix[j])
            i+=1
            j-=1
        res.append(prefix[i])

        return res
