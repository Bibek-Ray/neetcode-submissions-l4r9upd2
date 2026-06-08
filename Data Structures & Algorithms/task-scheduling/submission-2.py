import heapq as hq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ls = []
        freq = {}
        cooldown = deque()
        
        for val in tasks:
            if val in freq:
                freq[val] += 1
            else:
                freq[val] = 1
        
        for key, val in freq.items():
            ls.append((-val, key))
        
        hq.heapify(ls)

        t = 0

        while ls or cooldown:
            if cooldown and cooldown[0][0] == t:
                ready_time, count, task = cooldown.popleft()
                hq.heappush(ls, (count, task))

            if ls:
                val = hq.heappop(ls)
                new_count = val[0] + 1

                if new_count != 0:
                    cooldown.append((t + n + 1, val[0] + 1, val[1]))
            
            t += 1

        return t