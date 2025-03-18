class Solution1:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res=""
        for c in s:
            if c.isalnum():
                res += c
        return res == res[::-1]
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res = "".join(c for c in s if c.isalnum())
        reversed_res = "".join(res[i] for i in range(len(res)-1, -1, -1))
        return res == reversed_res
class Solution3:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res = "".join(c for c in s if c.isalnum())
        reversed_res = ""
        for c in res:
            reversed_res = c + reversed_res
        return res == reversed_res
