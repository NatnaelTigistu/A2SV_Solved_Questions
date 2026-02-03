class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        i = 0
        j = len(num)-1
        while j > i:
            if num[i] == num[j]:
                j -= 1 
                i += 1
            else: 
                return False
        return True