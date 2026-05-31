class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [[strs[0]]]
        new_strs = []
        for word in strs:
            new_strs.append("".join(sorted(word)))
        visited = [False] * len(strs)
        result = []

        for i in range(len(new_strs)):
            if visited[i]:
                continue
            group = [strs[i]]
            visited[i] = True

            for j in range(i + 1, len(new_strs)):
                if not visited[j] and new_strs[j] == new_strs[i]:
                    visited[j] = True
                    group.append(strs[j])
            result.append(group)

        return result

        
        