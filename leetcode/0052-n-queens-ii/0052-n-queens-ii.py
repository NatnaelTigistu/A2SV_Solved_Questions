class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        path = [""] * n
        col = set()
        ld = set()  
        rd = set()  

        def backtrack(row):
            nonlocal count
            if row == n:
                count += 1
                return

            for j in range(n):
                if j not in col and (row - j) not in ld and (row + j) not in rd:
                    path[row] = "." * j + "Q" + "." * (n - j - 1)
                    col.add(j)
                    ld.add(row - j)
                    rd.add(row + j)

                    backtrack(row + 1)  

                    col.remove(j)
                    ld.remove(row - j)
                    rd.remove(row + j)
                    path[row] = ""

        backtrack(0)
        return count