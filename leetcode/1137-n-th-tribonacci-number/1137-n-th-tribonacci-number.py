from collections import deque
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1 or n== 2: return 1
        prev = deque([0,1,1])
     
        while n > 3:
            new = sum(prev)
            prev.popleft()
            prev.append(new)
            n-=1
        return sum(prev)