class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:   # if left is less or equal to mid then obviously left to mid is sorted. Now we have target too, we need to see whether target is between left and mid(we can implement bs here)
                if nums[left] <= target and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:                         # if left is greater than mid then obviously mid to right is sorted, and comparing it with target will tell us where to search
                if nums[mid] <= target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1