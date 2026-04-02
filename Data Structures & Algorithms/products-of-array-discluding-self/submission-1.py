class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output = []
        before, after = nums.copy(), nums.copy()
        print(f"Before: {before}, After: {after}")

        for i in range(1, len(nums)):
            before[i] *= before[i-1]
            after[len(nums)-i-1] *= after[len(nums)-i]
        
        for i in range(len(nums)):
            if i-1 < 0:
                output.append(after[i+1])
            elif i+1 == len(nums):
                output.append(before[len(nums) - 2])
            else:
                output.append(before[i-1] * after[i+1])

        return output