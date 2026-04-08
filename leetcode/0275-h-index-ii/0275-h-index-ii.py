from typing import List
from collections import defaultdict

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        
        # FIX 1: correct search bounds
        _min = 0
        _max = n
        
        # FIX 2: build refere correctly
        refere = [0] * (n + 1)
        j = 0
        
        for h in range(n + 1):
            while j < n and citations[j] < h:
                j += 1
            refere[h] = n - j
        
        ans = 0
        
        # FIX 3: binary search condition + answer
        while _min <= _max:
            cite = (_min + _max) // 2
            
            if refere[cite] >= cite:
                ans = cite   # NOT refere[cite]
                _min = cite + 1
            else:
                _max = cite - 1
        
        return ans