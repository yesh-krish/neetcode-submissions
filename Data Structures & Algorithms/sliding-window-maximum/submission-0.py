class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        for i in range(len(nums) - k + 1):
            maxN = nums[i]
            for j in range(i, i + k):
                maxN = max(maxN,nums[j])
            res.append(maxN)
        return res

        