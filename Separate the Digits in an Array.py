class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            numDigit= []
            while num > 0:
                numDigit.append(num % 10)
                num = num // 10
            for i in numDigit[::-1]:
                res.append(i)
        return res