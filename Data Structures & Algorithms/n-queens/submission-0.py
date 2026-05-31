class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pos_D = set() #(r +c)
        neg_D = set() #(r -c)

        res = []

        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                 copy = ["".join(row) for row in board]
                 res.append(copy)
                 return
            for c in range(n):
                if c in col or (r+c) in pos_D or (r-c) in neg_D:
                    continue
                col.add(c)
                pos_D.add(r + c)
                neg_D.add(r-c)
                board[r][c] = "Q"
                backtrack(r + 1)
                col.remove(c)
                pos_D.remove(r + c)
                neg_D.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return res



        