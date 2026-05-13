class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        index = 0
        seen = set()
        while True:
            if nums[index] not in seen:
                seen.add(nums[index])
                index = nums[index]
            else:
                index = nums[index]
                break

        return index