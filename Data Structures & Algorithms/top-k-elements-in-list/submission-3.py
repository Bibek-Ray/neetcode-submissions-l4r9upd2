import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        bestk = [(0, 0)] * k
        heapq.heapify(bestk)
        topk = []

        for val in nums:
            if val in count:
                count[val] += 1
            else:
                count[val] = 1
        
        count = list(count.items())
        print(count)
                
        for val in count:
            if bestk[0][0] < val[1]:
                heapq.heappop(bestk)
                heapq.heappush(bestk, tuple(reversed(list(val))))
                
        for val in bestk:
            topk.append(val[1])
                
        return topk