class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0  # Start both pointers at the beginning
        length = 0
        seen = set()  # To track characters in the current window
        
        while r < len(s):
            if s[r] in seen:  # Duplicate found
                seen.remove(s[l])  # Remove the leftmost character
                l += 1  # Slide the left pointer forward
            else:
                seen.add(s[r])  # Add the character to the set
                curr = r - l + 1  # Calculate current window size
                length = max(length, curr)  # Update maximum length
                r += 1  # Expand the right pointer
        
        return length
