class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                collision_pt = slow
                break
        
        slow = 0
        
        while slow != collision_pt:
            slow = nums[slow]
            collision_pt = nums[collision_pt]

        return slow