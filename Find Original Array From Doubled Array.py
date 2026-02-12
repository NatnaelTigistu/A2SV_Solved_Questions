class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        
        if n % 2 != 0:
            return []
        
        changed.sort()
        freq = Counter(changed)
        original = []
        for x in changed:
            if freq[x] == 0:
                continue
            if freq[2 * x] == 0:
                return []
            original.append(x)
            freq[x] -=  1
            freq[x * 2] -= 1
        return original