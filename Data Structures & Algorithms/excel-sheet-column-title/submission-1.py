class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        result = ""
        while columnNumber > 0:
            columnNumber -= 1

            remainder = columnNumber % 26

            letter = chr(ord('A') + remainder)

            result = letter + result
            columnNumber //= 26
        return result