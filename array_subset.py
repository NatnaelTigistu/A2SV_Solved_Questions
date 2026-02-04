#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        freq = {}
        
        for i in a:
            freq[i] = freq.get(i,0) + 1
            
        for i in b:
            if i not in freq:
                return False
            freq[i] -= 1
            if freq[i] == 0:
                del freq[i]
        return True
    