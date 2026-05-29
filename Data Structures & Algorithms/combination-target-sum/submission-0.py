class Solution:
    def validate(self, nums, target, sm, subset, index):
        if target == 0:
            subset.append(list(sm))
            return

        if target < 0 or index >= len(nums):
            return
        
        sm.append(nums[index])

        self.validate(nums, target - nums[index], sm, subset, index)

        sm.pop()
        self.validate(nums, target, sm, subset, index + 1)
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sm = []
        subset = []

        self.validate(nums, target, sm, subset, 0)

        return subset