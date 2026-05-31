class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        cur = ""
        res = []
        j = len(digits)
        phonekey = {"2":"abc","3":"def","4":"ghi",
                    "5":"jkl","6":"mno","7":"pqrs",
                    "8":"tuv","9":"wxyz"}

        def phone(index,cur):
            if len(cur) == j:
                res.append(cur)
                return
            digit = digits[index]
            for letter in phonekey[digit]:
                phone(index + 1, cur + letter)
        phone(0,"")
        return res



    

        