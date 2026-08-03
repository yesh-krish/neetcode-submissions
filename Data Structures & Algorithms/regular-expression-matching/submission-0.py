class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = {}

        def dfs(i, j):
            # If we've reached the end of the pattern
            if j == n:
                return i == m

            if (i, j) in dp:
                return dp[(i, j)]

            match = False
            if i < m and (s[i] == p[j] or p[j] == "."):
                match = True

            # Handle '*' case
            if (j + 1) < n and p[j + 1] == "*":
                # Option 1: skip the '*' (move past j+2)
                # Option 2: use the '*' if there's a match (stay at j, move i+1)
                dp[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return dp[(i, j)]
            else:
                if match:
                    dp[(i, j)] = dfs(i + 1, j + 1)
                    return dp[(i, j)]

            dp[(i, j)] = False
            return False

        return dfs(0, 0)
