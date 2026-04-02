class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {")": "(", "}": "{", "]": "["}
        
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if stack and stack[-1] == mp[ch]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0