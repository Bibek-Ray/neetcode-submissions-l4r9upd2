class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_idx = 0
        right_idx = len(nums) - 1
        mid_idx = (left_idx + right_idx) // 2

        while left_idx <= right_idx:
            mid_idx = (left_idx + right_idx) // 2
            if nums[mid_idx] == target:
                return mid_idx
            elif nums[mid_idx] > target:
                right_idx = mid_idx - 1
            else:
                left_idx = mid_idx + 1

        return -1