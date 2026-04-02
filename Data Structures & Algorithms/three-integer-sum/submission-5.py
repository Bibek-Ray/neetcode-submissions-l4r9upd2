class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        left = 0
        right = len(nums) - 1
        res = []
        res_id = []
        nums.sort()
        for i in range(len(nums)-1):
            target = (-1) * nums[i]
            left = i+1
            right = len(nums) - 1
            while True:
                if left<right:
                    if nums[left] + nums[right] > target:
                        right -= 1
                    elif nums[left] + nums[right] < target:
                        left += 1
                    elif nums[left] + nums[right] == target:
                        res_id = [(-1)*target, nums[left], nums[right]]
                        if res_id not in res:
                            res.append(res_id)
                        right -= 1
                        left += 1
                    else:
                        continue
                else:
                    break
                    
        return res