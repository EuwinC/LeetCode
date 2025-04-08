class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = collections.Counter(t)
        need,have = len(count_t),0
        count_s = collections.defaultdict(int)
        window_size = len(t)
        i,j = 0,0
        res = [0,float("inf")]
        for c in s:
            count_s[c] = count_s.get(c,0) +1
            if c in count_t and count_s[c] == count_t[c]:
                have +=1
            
            while have == need:
                res = [i,j+1] if (j-i+1) < res[1]-res[0] else res
                count_s[s[i]] -=1
                if s[i] in count_t and count_s[s[i]] < count_t[s[i]]:
                    have -=1
                i += 1
            j+=1
        return s[res[0]:res[1]] if res[1] != float("inf") else ""
               
