import heapq as hq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ls = []
        op = []

        for coor in points:
            ls.append(((coor[0]**2 + coor[1]**2), coor))

        hq.heapify(ls)

        for i in range(k):
            op.append(hq.heappop(ls)[1])

        return op