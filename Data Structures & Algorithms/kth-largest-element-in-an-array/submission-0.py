import heapq as hq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ls = [-x for x in nums]
        hq.heapify(ls)

        for i in range(k):
            val = -hq.heappop(ls)
        
        return val