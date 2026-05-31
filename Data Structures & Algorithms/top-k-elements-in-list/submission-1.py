from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = Counter(nums)

        for item, frequency in count.most_common(k):
            res.append(item)
        return res