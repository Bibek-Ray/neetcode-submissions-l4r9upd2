class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):

            while len(stack) != 0 and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if len(stack) == 0:
                result[i] = 0

            else:
                result[i] = stack[-1] - i

            stack.append(i)
            print(stack)
        return result
