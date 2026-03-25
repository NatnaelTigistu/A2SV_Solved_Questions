class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(s,prev = None):
            if int(s) == prev -1:
                return True
            for i in range(1,len(s)):
                curr = int(s[:i])
                if curr == prev -1 and backtrack(s[i:],curr) :
                    return True
                elif curr >= prev:
                    break
            return False
        for i in range(1,len(s)):
            if backtrack(s[i:],int(s[:i])): 
                return True
        return False
            
            
