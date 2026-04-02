class Solution:
    def createFreqMap(self, s: str) -> dict:        
        dct = {}

        for ch in s:
            if ch not in dct:
                dct[ch] = 1
            else:
                dct[ch] += 1

        return dct

    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        flag = False
        s1_map = self.createFreqMap(s1)
        for i in range(len(s2) - k + 1):
            if self.createFreqMap(s2[i: i+k]) == s1_map:
                flag = True
                break
        
        return flag