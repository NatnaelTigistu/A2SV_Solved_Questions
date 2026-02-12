class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}
        mark = n
        while True:
            total = 0
            while n > 0:
                digit = n % 10
                total += digit*digit
                n = n // 10
            n = total

            if n == 1:
                return True
            if n not in seen:
              seen[n] = True
            else:
                return False
        return False