class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)
        set1 = set()
        answer = []

        l = len(nums)

        for n in nums:
            if n in set1:
                counter[n] += 1
            else:
                set1.add(n)
                counter[n] += 1

            if counter[n] > (l // 3):
                if n not in answer:
                    answer.append(n)

        return answer