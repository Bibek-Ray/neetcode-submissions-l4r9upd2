class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        topk = []

        for val in nums:
            if val in count:
                count[val] += 1
            else:
                count[val] = 1
                
        count = sorted(count.items(), key=lambda item:item[1], reverse=True)
        
        for i in range(k):
            topk.append(count[i][0])
        
        return topk