class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new_nums = set(nums)
        hashset = Counter(nums)
        b = sorted(new_nums, key = lambda n: hashset[n], reverse = True)
        res = []
        for i in range(0,k):
            res.append(b[i])

        return res
        