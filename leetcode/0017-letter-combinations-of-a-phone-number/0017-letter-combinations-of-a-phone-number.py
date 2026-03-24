class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        res = [str(char) for char in digit_to_letters[digits[0]]]
        def helper(digit,res):
            temp = []
            for char in digit_to_letters[digit]:
                for s in res:
                    temp.append(s+str(char))
            res = temp
            return res

        for digit in digits[1:]:
            res = helper(digit,res)

        return res
