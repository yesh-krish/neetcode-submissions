from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = stoneSum // 2
        dp = {}

        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (stoneSum - total))
            if (i, total) in dp:
                return dp[(i, total)]
            
            # Explore two choices: skip or take current stone
            take = dfs(i + 1, total + stones[i])
            skip = dfs(i + 1, total)
            
            dp[(i, total)] = min(skip, take)
            return dp[(i, total)]

        return dfs(0, 0)
