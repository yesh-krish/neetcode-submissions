from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, total):
            if total == 0:
                return 1

            if total < 0 or i == len(coins):
                return 0

            if (i, total) in memo:
                return memo[(i, total)]

            memo[(i, total)] = (
                dfs(i, total - coins[i])     # use current coin again
                + dfs(i + 1, total)          # skip current coin
            )

            return memo[(i, total)]

        return dfs(0, amount)