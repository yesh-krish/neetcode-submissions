class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = ""
        for char in s:
            if char.isalnum():
                filtered_s += char.lower()
        l = 0
        r = len(filtered_s) - 1
        while l < r:
            if filtered_s[l] != filtered_s[r]:
                return False
            l +=1
            r -=1
        return True
        