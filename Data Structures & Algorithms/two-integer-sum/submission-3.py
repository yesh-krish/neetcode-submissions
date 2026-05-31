class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        length = len(nums)
        for i in range(length):
            x = target - nums[i]
            if x in hashmap:
                return [hashmap[x],i]
            hashmap[nums[i]] = i
        