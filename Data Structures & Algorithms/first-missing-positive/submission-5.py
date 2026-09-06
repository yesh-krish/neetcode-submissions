class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        arr = [0] * len(nums)

        for n in nums:
            if 1 <= n <= len(nums):
                arr[n - 1] = 1
        for i in range(len(arr)):
            if arr[i] == 0:
                return i + 1
        return len(nums) + 1
        