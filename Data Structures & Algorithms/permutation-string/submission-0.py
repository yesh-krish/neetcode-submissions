from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length1, length2 = len(s1), len(s2)

        if length1 > length2:
            return False  # If s1 is longer than s2, permutation is impossible

        freq_s1 = Counter(s1)  # Frequency count of characters in s1
        freq_window = Counter(s2[:length1])  # Frequency count of first window in s2

        if freq_s1 == freq_window:
            return True  # If first window matches, return True

        for i in range(length1, length2):
            # Add the new character in the window
            freq_window[s2[i]] += 1

            # Remove the character that is now out of the window
            freq_window[s2[i - length1]] -= 1

            # If the frequency becomes zero, remove the character from the dictionary
            if freq_window[s2[i - length1]] == 0:
                del freq_window[s2[i - length1]]

            # Check if updated window matches s1's frequency
            if freq_s1 == freq_window:
                return True

        return False  # No valid permutation found
