class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i,n in enumerate(nums):
            x = target - n
            if x in hashset:
                return [hashset[x], i]
            hashset[n] = i

        return False

