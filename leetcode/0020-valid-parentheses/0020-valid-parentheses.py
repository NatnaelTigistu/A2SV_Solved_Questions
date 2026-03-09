class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:

            if bracket == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
            elif bracket == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()
            elif bracket == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()
            else:
                stack.append(bracket)
        return not stack