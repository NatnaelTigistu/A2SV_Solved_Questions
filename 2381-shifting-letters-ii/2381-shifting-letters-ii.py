from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)

        for l, r, d in shifts:
            if d == 1:   # forward shift
                diff[l] += 1
                if r + 1 < n:
                    diff[r + 1] -= 1
            else:        # backward shift
                diff[l] -= 1
                if r + 1 < n:
                    diff[r + 1] += 1

        result = []
        shift = 0

        # Apply prefix sum and shift characters
        for i in range(n):
            shift += diff[i]
            new_char = (ord(s[i]) - ord('a') + shift) % 26
            result.append(chr(new_char + ord('a')))

        return "".join(result)