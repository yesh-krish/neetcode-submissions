class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)
        res = 0

        def backtrack(r):
            nonlocal res
            if r == n:
                res += 1
                return

            for c in range(n):
                # Check if the column or either diagonal is under attack
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                # "Choose" - Add to sets
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                
                # "Explore" - Move to the next row
                backtrack(r + 1)
                
                # "Un-choose" - Backtrack (Cleanup)
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(0)
        return res