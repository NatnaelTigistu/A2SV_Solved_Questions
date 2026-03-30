class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        #115358
        greater = False
        valid = False
        def check(s,path):
            nonlocal valid,greater
            print(s,path)
            if len(path) > 2:
                for i in range(2,len(path)):
                    if path[i] != path[i-1] + path[i-2]:
                        if path[i] > path[i-1] + path[i-2]:
                            greater = True
                        return
                if s == len(num):
                    valid = True
                    return
            
            for i in range(s,len(num)):
                if num[s] == '0' and i != s:
                    return
                path.append(int(num[s:i+1]))
                check(i+1,path)
                path.pop()
                if greater:
                    greater = False
                    return
                if valid :
                    return
        check(0,[])
        return valid