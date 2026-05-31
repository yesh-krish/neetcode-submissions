class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        indices = {}
        for word in strs:
            key = tuple(sorted(word))  # use tuple (hashable)
            if key not in indices:
                indices[key] = []
            indices[key].append(word)
        
        return list(indices.values())
