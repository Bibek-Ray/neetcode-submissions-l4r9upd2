class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxx  = 0

        for idx, val in enumerate(prices):
            for j in range(idx+1, len(prices)):
                if prices[j] > val:
                    if prices[j] - val > maxx:
                        maxx = prices[j] - val
                else:
                    continue
        
        return maxx