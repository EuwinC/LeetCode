class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = deque()
        res = 0
        ch = set()
        for c in s:
            while c in ch:
                ch.remove(window.popleft())
            ch.add(c)
            window.append(c)
            res = max(res, len(window))
        return res

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        sub_dict = dict()
        l,r =0,0


        res = 0
        while r < len(s):
            
            if s[r] in sub_dict and sub_dict[s[r]] >= l:
                l = sub_dict.get(s[r])+1
            res = max(res,(r-l)+1)
            sub_dict[s[r]] = r
            
            r += 1
        
        return res

