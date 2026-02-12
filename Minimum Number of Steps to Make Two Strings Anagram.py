class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = Counter(s)
        steps = 0
        
        for c in t:
            if count[c] > 0:
                count[c] -= 1
            else:
                steps += 1
                
        return steps