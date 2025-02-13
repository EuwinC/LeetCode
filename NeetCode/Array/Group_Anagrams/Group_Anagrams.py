import collections
class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)

        for s in strs: #O(N)
            list_s = list(s) 
            list_s.sort() #O(Nlog(N))
            list_s = "".join(list_s)
            hashmap[list_s].append(s)
        res =[]
        for anagram in hashmap: #O(N)
            res.append(hashmap.get(anagram))
        return res

class Solution2:
    def groupAnagrams(self, strs) -> List[List[str]]:

        res =defaultdict(list)

        for s in strs: #O(N)
            freq = [0] * 26
            for c in s: #O(N)
                freq[ord(c)-ord('a')] +=1
            res[tuple(freq)].append(s)
        return res.values()

        
