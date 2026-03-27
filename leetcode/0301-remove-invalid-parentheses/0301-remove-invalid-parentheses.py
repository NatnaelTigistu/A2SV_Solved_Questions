class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n = len(s)
        _max = 0
        res = set()
        visited = set()

        def backtrack(path, st, op, cl):
            nonlocal _max, res
            
            # include path in state to avoid wrong pruning
            state = (st, op, cl, tuple(path))
            if state in visited:
                return
            visited.add(state)

            # invalid case
            if cl > op:
                return

            # update result
            if op == cl:
                if len(path) > _max:
                    res.clear()
                    res.add("".join(path))
                    _max = len(path)
                elif len(path) == _max:
                    res.add("".join(path))

            if st == n:
                return

            for i in range(st, n):
                path.append(s[i])

                if s[i] == '(':
                    backtrack(path, i + 1, op + 1, cl)

                elif s[i] == ')':
                    backtrack(path, i + 1, op, cl + 1)

                else:
                    backtrack(path, i + 1, op, cl)

                path.pop()

        backtrack([], 0, 0, 0)
        return list(res)