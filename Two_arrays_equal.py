class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        if len(a) != len(b):
            return False
            
        setA = {}
        for i in a:
            setA[i] = setA.get(i,0) + 1
        for i in b:
            if i not in setA:
                return False
            setA[i] = setA[i] - 1
            if setA[i] == 0:
                del setA[i]
        return True