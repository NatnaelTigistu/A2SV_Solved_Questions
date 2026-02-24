class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        b = int(sqrt(c))
        a = 0
        while a <= b:
            current = a*a + b*b
            if current == c:
                return True
            elif current < c:
                a += 1
            else:
                b -= 1
        return False