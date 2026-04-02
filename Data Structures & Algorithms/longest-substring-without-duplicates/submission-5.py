class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls = list(s)
        left = 0
        mx = 1
        right = 1

        if len(s) > 0:
            while right < len(ls):
                print(ls[left: right])
                if s[right] not in ls[left: right]:
                    right += 1
                    mx = max(mx, (right - left))
                else:
                    left += 1
        else:
            mx = 0
        return mx