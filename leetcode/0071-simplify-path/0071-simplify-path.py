class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        print(path)
        res = []
        for p in path:
            if not p:
                continue
            elif p == '..' and res:
                res.pop()
            elif p == '..':
                continue
            elif p == '.':
                continue
            else:
                res.append('/' + p)
            print(res)
        if not res:
            return "/"
        return ''.join(res)