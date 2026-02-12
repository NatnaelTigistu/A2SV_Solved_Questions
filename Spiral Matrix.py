class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        rows = len(matrix)
        cols = len(matrix[0])

        sideWay = cols
        vertical = rows - 1

        total = rows * cols
        res = [0] * total
        pos = 0

        def lTor(i, j):
            nonlocal sideWay, pos
            for _ in range(sideWay):
                res[pos] = matrix[i][j]
                pos += 1
                j += 1

            if pos >= total:
                return
            sideWay -= 1
            tTob(i + 1, j - 1)

        def tTob(i, j):
            nonlocal vertical, pos
            for _ in range(vertical):
                res[pos] = matrix[i][j]
                pos += 1
                i += 1
            
            vertical -= 1
            rTol(i - 1, j - 1)

        def rTol(i, j):
            nonlocal sideWay, pos
            for _ in range(sideWay):
                res[pos] = matrix[i][j]
                pos += 1
                j -= 1

            if pos >= total:
                return
            sideWay -= 1
            bTot(i - 1, j + 1)

        def bTot(i, j):
            nonlocal vertical, pos
            for _ in range(vertical):
                res[pos] = matrix[i][j]
                pos += 1
                i -= 1

            vertical -= 1
            lTor(i + 1, j + 1)

        lTor(0, 0)
        return res
