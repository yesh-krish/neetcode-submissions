class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if target == "0000":
            return 0
        visits = set(deadends)

        if "0000" in visits:
            return -1
        
        q = deque(["0000"])
        visits.add("0000")

        steps = 0

        while q:
            steps += 1

            for _ in range(len(q)):
                lock = q.popleft()
                for i in range(4):
                    for j in [1,-1]:
                        digit = str((int(lock[i]) + j + 10) % 10)
                        nextlock= lock[:i] + digit + lock[i + 1:]
                        if nextlock in visits:
                            continue
                        if nextlock == target:
                            return steps
                        q.append(nextlock)
                        visits.add(nextlock)
        return -1 




        

        