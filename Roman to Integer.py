class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        n = 0
        def rtod(s,n,number) -> int:
            if n == len(s):
                return 0
            elif s[n] == "M":
                number = 1000 
                return number + rtod(s,n+1,number)
            elif s[n] == "D":
                number = 500 
                return number + rtod(s,n+1,number)
            elif s[n] == "C":
                if n + 1 < len(s) and s[n+1]:
                    if s[n+1] == "D":
                        number = 400 
                        return number + rtod(s,n+2,number)
                    elif s[n+1] == "M":
                        number = 900 
                        return number + rtod(s,n+2,number)
                    else :
                        number = 100 
                        return number + rtod(s,n+1,number)
                else :
                    number = 100 
                    return number + rtod(s,n+1,number)
            elif s[n] == "L":
                number = 50 
                return number + rtod(s,n+1,number)
            elif s[n] == "X":
                if n + 1 < len(s) and s[n+1]:
                    if s[n+1] == "L":
                        number = 40
                        return number + rtod(s,n+2,number)
                    elif s[n+1] == "C":
                        number = 90 
                        return number + rtod(s,n+2,number)
                    else :
                        number = 10 
                        return number + rtod(s,n+1,number)
                else :
                    number = 10 
                    return number + rtod(s,n+1,number)
            elif s[n] == "V":
                number = 5 
                return number + rtod(s,n+1,number)
            elif s[n] == "I":
                if n + 1 < len(s) and s[n+1]:
                    if s[n+1] == "V":
                        number = 4 
                        return number + rtod(s,n+2,number)
                    elif s[n+1] == "X":
                        number = 9 
                        return number + rtod(s,n+2,number)
                    else :
                        number = 1 
                        return number + rtod(s,n+1,number)
                else :
                    number = 1 
                    return number + rtod(s,n+1,number)
            else:
                return -1
        number = rtod(s,n,number)
        return number