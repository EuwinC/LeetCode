class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        fre_s1 = [0] *26
        fre_s2 = [0] * 26
        
        for c in s1:
            fre_s1[ord(c)-ord("a")] +=1
        
        window_size = len(s1)

        i,j = 0,0

        for c in s2:
            fre_s2[ord(c)-ord("a")] +=1
            if (j-i + 1) == window_size:
                if fre_s2 == fre_s1:
                    return True
                fre_s2[ord(s2[i])-ord("a")] -=1
                i +=1
            j+=1
        return False
