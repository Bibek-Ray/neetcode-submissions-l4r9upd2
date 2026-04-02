class Solution:
    def maxArea(self, heights: list[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1
        height = 0
        maxx = 0

        for i in range(len(heights)):
            if p1 < p2:
                height = min(heights[p1], heights[p2])
                area = height * (p2 - p1)
                if area > maxx:
                    maxx = area
                if heights[p1] < heights[p2]:
                    p1 += 1
                else:
                    p2 -= 1
            
        return maxx