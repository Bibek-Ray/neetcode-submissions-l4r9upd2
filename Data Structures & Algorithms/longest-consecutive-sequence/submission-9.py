class Solution:
    def testRecur(self, num: dict, start: int) -> int:
        
        if (start+1) in num.keys():
            return self.testRecur(num, start+1) + 1
        else:
            return 1
                
        
    def longestConsecutive(self, nums: list[int]) -> int:
        num = list(set(nums))
        ref = {}
        maxx = 0
        
        for val in num:
            ref[val] = 0
            
        for idx in ref.keys():
            if (idx-1) not in ref.keys():
                if self.testRecur(ref, idx) > maxx:
                    maxx = self.testRecur(ref, idx)
                
        return maxx