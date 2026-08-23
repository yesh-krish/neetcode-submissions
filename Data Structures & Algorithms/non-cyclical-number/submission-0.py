class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = set()
        cycle.add(n)

        def cyc(n):
            digit_sum = sum(int(digit) ** 2 for digit in str(n))

            if digit_sum == 1:
                return True
            elif digit_sum in cycle:
                return False
            else:
                cycle.add(digit_sum)
                return cyc(digit_sum)

        return cyc(n)