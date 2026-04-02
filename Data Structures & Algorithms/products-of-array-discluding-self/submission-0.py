class Solution:
    def product(self, start: int, end: int, nums: list[int]) -> int:
        prod = 1
        
        if end < start or start > (len(nums)):
            return 1

        for i in range(start, end):
            prod *= nums[i]

        return prod

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output = []

        for i in range(len(nums)):
            output.append(self.product(0, i, nums) * self.product(i+1, len(nums), nums))

        return output