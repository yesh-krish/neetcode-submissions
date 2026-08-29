class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []

        output = 0

        for s in operations:
            if s == "+":
                stack.append(stack[-1] + stack[-2])
            elif s == "D":
                stack.append(2 * stack[-1])
            elif s == "C":
                stack.pop()
            else:
                stack.append(int(s))

        return sum(stack)



        