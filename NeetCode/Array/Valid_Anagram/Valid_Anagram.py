class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        t_count = {i:0 for i in range(26)} #O(26) O(26)
        s_count = {i:0 for i in range(26)} #O(26) O(26)

        for i in range(len(t)): #O(N)
            t_count[ord(t[i])-ord('a')] +=1
            s_count[ord(s[i])-ord('a')] +=1

        return t_count == s_count #O(N) O(26)

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        s,t = list(s),list(t) #O(N) O(N)
        s.sort() #Nlog(N) O(1)
        t.sort() #Nlog(N) O(1)
        return s == t 
