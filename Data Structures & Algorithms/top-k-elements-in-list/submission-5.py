class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            hashset = Counter(nums)
            b = list(hashset.keys())
            b.sort(key = lambda n: hashset[n], reverse = True)
            x = []
            for i in range(0,k):
                x.append(b[i])

            return x



        