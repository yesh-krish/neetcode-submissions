class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        word_set = set(dictionary)
        # dp[i] = min extra chars for suffix s[i:]
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            # Default: current char is "extra"
            dp[i] = 1 + dp[i + 1]
            
            # Try all possible substrings starting at i
            for j in range(i, n):
                substring = s[i : j + 1]
                if substring in word_set:
                    dp[i] = min(dp[i], dp[j + 1])
                    
        return dp[0]