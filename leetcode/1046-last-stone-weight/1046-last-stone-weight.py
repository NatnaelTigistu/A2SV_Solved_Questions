import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            heapq.heapify_max(stones)
            y = heapq.heappop_max(stones)
            x = heapq.heappop_max(stones)
            print(y,x)
            if y-x > 0: heapq.heappush_max(stones,y-x)
        if stones: return stones[0]
        else: return 0