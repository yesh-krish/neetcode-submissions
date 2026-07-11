class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[-1] * n for _ in range(m)]

    
        def dfs(j,k):
            if j == m - 1 and k == n - 1:
                return 1
            if j >= m or k >= n:
                return 0
            if dp[j][k] != -1:
                return dp[j][k]
            dp[j][k] = dfs(j, k + 1) + dfs(j + 1, k)
            return dp[j][k]
        return dfs(0,0)
            

        