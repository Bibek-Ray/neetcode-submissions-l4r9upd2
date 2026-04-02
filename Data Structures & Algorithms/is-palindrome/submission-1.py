class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        wd = []
        wd_reverse = []
        
        for i in range(len(s)):
            if s[i].isalnum():
                wd.append(s[i])

        wd_reverse = wd[::-1]
        if wd == wd_reverse:
            return True
        else:
            return False