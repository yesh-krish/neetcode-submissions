class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D, R = deque(), deque()
        n = len(senate)

        for i, c in enumerate(senate):
            if c == "R":
                R.append(i)
            else:
                D.append(i)
        while D and R:
            Dturn = D.popleft()
            Rturn = R.popleft()

            if Rturn < Dturn:
                R.append(Rturn + n)
            else:
                D.append(Dturn + n)
        return "Radiant" if R else "Dire"

        

        