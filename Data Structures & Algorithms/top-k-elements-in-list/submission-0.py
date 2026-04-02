class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        topk = []

        for val in nums:
            if val in count:
                count[val] += 1
            else:
                count[val] = 1
        
        for i in range(k):
            max_val = max(count, key=count.get)
            topk.append(max_val)
            del count[max_val]
        
        return topk