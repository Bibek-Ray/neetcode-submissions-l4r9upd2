class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        k = 1
        c = 0

        while len(temperatures) > 1:
            
            if temperatures[k] > temperatures[0]:
                result[c] = k
                c += 1
                k = 1
                temperatures.pop(0)
            elif k >= len(temperatures) - 1:
                c += 1
                k = 1
                temperatures.pop(0)
            else:
                k += 1
        
        return result