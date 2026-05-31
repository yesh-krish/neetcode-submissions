from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_dict = defaultdict(list)
        
        for i, n in enumerate(strs):
            sorted_str = ''.join(sorted(n))  # Sort the string and join back to a single string
            new_dict[sorted_str].append(i)   # Append the index to the corresponding sorted string key

        grouped = []

        for indices in new_dict.values():
            group = [strs[i] for i in indices]  # Create a group using the indices from the original list
            grouped.append(group)

        return grouped