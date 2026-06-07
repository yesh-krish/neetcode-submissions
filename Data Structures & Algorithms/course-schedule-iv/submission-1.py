from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[u].append(v)
            
        is_prereq = [[False] * numCourses for _ in range(numCourses)]
        
        def dfs(start, curr):
            # Fixed the typo here: changed 'neighbour' to 'neighbor'
            for neighbor in adj[curr]:
                if not is_prereq[start][neighbor]:
                    is_prereq[start][neighbor] = True
                    dfs(start, neighbor)
                    
        for i in range(numCourses):
            dfs(i, i)
            
        return [is_prereq[u][v] for u, v in queries]