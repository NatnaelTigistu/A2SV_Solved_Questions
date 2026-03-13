class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for b in s:
            if b == ")":

                if stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                else:
                    k = 0
                    while stack[-1] != "(":
                        k = int(stack.pop()) + k
                    stack.pop()
                    k = 2*k
                    stack.append(k)
                    
            else:
                stack.append(b)

        return sum(stack)