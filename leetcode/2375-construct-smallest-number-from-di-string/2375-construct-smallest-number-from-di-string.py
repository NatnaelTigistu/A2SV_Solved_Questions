class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = ""
        s = ['1']
        for i in range(len(pattern)):
            if pattern[i] == 'I':
                while s:
                    res += s.pop()
            s.append(chr(i + ord('2')))
        while s: res += s.pop()
       
        return res