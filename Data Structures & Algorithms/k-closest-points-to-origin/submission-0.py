import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        for i in range(len(points)):
            vertex = points[i]
            x, y = vertex

            dist = math.sqrt((0 - x)**2 + (0-y)**2)
            res.append((dist,vertex))
        res.sort(key =lambda x: x[0])
        result = [point for _,point in res[:k]]
        return result