class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currentSum = 0
        prefixSum = {0 : 1}
        count = 0

        for num in nums:
            currentSum += num
            difference = currentSum - k

            if difference in prefixSum:
                count += prefixSum[difference]

            prefixSum[currentSum] = prefixSum.get(currentSum,0) + 1

        return count

