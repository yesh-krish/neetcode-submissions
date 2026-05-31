class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)

        for item, count in count.items():
            if count > 1:
                return item


        