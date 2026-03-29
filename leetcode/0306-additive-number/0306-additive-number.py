class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        valid = False
        def backtrack(start,path):
            nonlocal valid

            if len(path) > 2:
                for i in range(2,len(path)):
                    if path[i] != path[i-1] + path[i-2]:
                        return
                if start == len(num):
                    valid = True
                    return
            
            for i in range(start,len(num)):
                if num[start] == '0' and i != start: return
                digit = int(num[start:i+1])
                path.append(digit)
                backtrack(i+1,path)
                if valid: return
                path.pop()
        backtrack(0,deque())
        return valid
                