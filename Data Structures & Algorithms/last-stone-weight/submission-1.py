import heapq as hq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        hq.heapify(max_heap)

        while len(max_heap) > 1:
            y = -hq.heappop(max_heap)
            x = -hq.heappop(max_heap)
            if x < y:
                y -= x
                hq.heappush(max_heap, -y)

        return -max_heap[0] if len(max_heap) != 0 else 0        
