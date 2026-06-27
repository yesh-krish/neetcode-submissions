class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s): True}
        wordSet = set(wordDict)

        def dfs(i):
            if i in memo:
                return memo[i]
            for j in range(i, len(s)):
                if s[i:j + 1] in wordSet:
                    if dfs(j + 1):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        return dfs(0)