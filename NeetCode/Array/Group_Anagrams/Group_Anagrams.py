import collections
class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)

        for s in strs:
            list_s = list(s)
            list_s.sort()
            list_s = "".join(list_s)
            hashmap[list_s].append(s)
        res =[]
        for anagram in hashmap:
            res.append(hashmap.get(anagram))
        return res

class Solution2(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        res =defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c)-ord('a')] +=1
            res[tuple(freq)].append(s)
        return res.values()

        
