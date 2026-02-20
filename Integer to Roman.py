class Solution:
    def intToRoman(self, num: int) -> str:
        symbol = {}
        symbol[1] = 'I'                    
        symbol[5] = 'V'
        symbol[10] = 'X'
        symbol[50] = 'L'
        symbol[100] = 'C'
        symbol[500] = 'D'
        symbol[1000] = 'M'
    
        i = 0
        roman = []
        while num > 0:
            reminder = num % 10
            if reminder == 4:
                roman.append(symbol[5*(10**i)])
                roman.append(symbol[1*(10**i)])
            elif reminder == 9:
                roman.append(symbol[10*(10**i)])
                roman.append(symbol[1*(10**i)])
            elif reminder == 5:
                roman.append(symbol[5*(10**i)])
            elif reminder == 0:
                num = num // 10
                i += 1
                continue
            elif reminder in (1,2,3):
                for _ in range(reminder):
                    roman.append(symbol[1*(10**i)])
            else:
                for _ in range(reminder - 5):
                    roman.append(symbol[1*(10**i)])
                roman.append(symbol[5*(10**i)])
            num = num // 10
            i += 1
        return ''.join(char for char in roman[::-1])