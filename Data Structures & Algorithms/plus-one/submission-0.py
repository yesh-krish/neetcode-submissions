class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        str1 = ""

        for num in digits:
            str1 += str(num)

        str2 = int(str1)

        str2 += 1

        str3 = str(str2)
        arr = []
        for num in str3:
            arr.append(int(num))      

        return arr