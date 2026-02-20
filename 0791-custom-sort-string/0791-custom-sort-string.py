class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orderPos = {}
        for i,char in enumerate(order):
            orderPos[char] = i
        
        appeared = []
        not_appeared = []

        for char in s:
            if char in orderPos:
                appeared.append(char)
            else:
                not_appeared.append(char)
        appeared.sort(key = lambda c : orderPos[c])
        return ''.join(c for c in appeared) + ''.join(c for c in not_appeared)