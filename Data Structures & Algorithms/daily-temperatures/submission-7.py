class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        for i in range(len(result)):
            for j in range(i+1, len(result)):
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i
                    break
        
        return result  