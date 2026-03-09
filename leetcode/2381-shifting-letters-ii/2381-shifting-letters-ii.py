from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift = [0] * (n+1)

        for l,r,d in shifts:
            if d == 0:
                shift[l] -= 1
                shift[r+1] += 1
            else:
                shift[l] += 1
                shift[r+1] -= 1
        _sum = 0
        for i in range(n):
            _sum += shift[i]
            shift[i] = _sum
        res = []
        _a = ord('a')
        for i in range(n):
            char = (ord(s[i]) - _a + shift[i]) % 26
            res.append(chr(char + _a))
        return ''.join(res)