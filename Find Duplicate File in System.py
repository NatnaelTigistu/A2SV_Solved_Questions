class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        m = {}
        for p in paths:
            parts = p.split()
            d = parts[0]
            for f in parts[1:]:
                i = f.index('(')
                name = f[:i]
                content = f[i+1:-1]
                path = d + '/' + name
                if content in m:
                    m[content].append(path)
                else:
                    m[content] = [path]
        res = []
        for v in m.values():
            if len(v) > 1:
                res.append(v)
        return res
