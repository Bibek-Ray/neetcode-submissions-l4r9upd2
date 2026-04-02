class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num = list(set(nums))
        num.sort()
        counter = 0
        maxx = 0
        print(num)
        
        for i in range(1, len(num)):
            if num[i] == (num[i-1] + 1):
                counter += 1
                if maxx < counter:
                    maxx = counter
            else:
                counter = 0
                
        if len(num) != 0:
            return maxx + 1
        else:
            return 0