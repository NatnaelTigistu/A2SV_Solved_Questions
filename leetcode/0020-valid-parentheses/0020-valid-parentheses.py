class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if not stack:
                stack.append(bracket)
            elif stack[-1] in [')',']','}']:
                return False
            elif bracket == ')' and stack[-1] == '(':
                stack.pop()
            elif bracket == ']' and stack[-1] == '[':
                stack.pop()
            elif bracket == '}' and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(bracket)
        return not stack