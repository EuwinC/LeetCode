class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0

        counter = collections.defaultdict(int)
        res = 0
        for c in s:
            counter[c] = counter.get(c,0) + 1
            while (r-l+1) - max(counter.values()) > k:
                counter[s[l]]  -= 1
                l += 1
            res = max(res,(r-l+1))
            
            r += 1
        return res
