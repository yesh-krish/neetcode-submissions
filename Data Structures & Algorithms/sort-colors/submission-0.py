class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        stackRed = []
        stackWhite = []
        stackBlue = []

        for num in nums:
            if num == 1:
                stackWhite.append(1)
            elif num == 0:
                stackRed.append(0)
            elif num == 2:
                stackBlue.append(2)

        nums[:] = stackRed + stackWhite + stackBlue

        