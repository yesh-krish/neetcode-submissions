class Solution:
    def partition(self, s: str) -> List[List[str]]:
        cur = []
        res = []
        def backtrack(i):
            if i >= len(s):
                res.append(cur.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s,i,j):
                    cur.append(s[i:j + 1])
                    backtrack(j + 1)
                    cur.pop()
        
        backtrack(0)
        return res
    def isPali(self,s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i,j = i +1, j -1
            return True
