class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        defDict = defaultdict(int)
        for number in nums:
            defDict[number] += 1
        return sorted(defDict, key=defDict.get, reverse=True)[:k]
