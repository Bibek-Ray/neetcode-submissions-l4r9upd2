import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        summ = 0
        left_idx = 1
        right_idx = max(piles) # 4
        while left_idx < right_idx:
            mid = (left_idx + right_idx) // 2
            summ = 0
            for val in piles:
                summ += math.ceil(val/mid)

            if summ <= h:
                right_idx = mid
            elif summ > h:
                left_idx = mid + 1

        return left_idx