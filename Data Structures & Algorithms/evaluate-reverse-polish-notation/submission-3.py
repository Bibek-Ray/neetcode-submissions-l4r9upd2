class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for val in tokens:
            if val in "+-*/":
                v1, v2 = stack[-2], stack[-1]
                if val == "+":
                    stack.pop()
                    stack.pop()
                    stack.append(v1 + v2)
                elif val == "-":
                    stack.pop()
                    stack.pop()
                    stack.append(v1 - v2)
                elif val == "*":
                    stack.pop()
                    stack.pop()
                    stack.append(v1 * v2)
                else:
                    stack.pop()
                    stack.pop()
                    stack.append(int(v1 / v2))
            else:
                stack.append(int(val))
        
        return stack[-1]