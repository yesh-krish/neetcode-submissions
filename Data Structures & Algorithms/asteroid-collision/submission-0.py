class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        
        for asteroid in asteroids:
            # A collision only occurs if stack[-1] moves right (> 0) 
            # and current asteroid moves left (< 0)
            while stack and asteroid < 0 < stack[-1]:
                diff = asteroid + stack[-1]
                if diff < 0:
                    # Current asteroid is larger; top of stack explodes
                    stack.pop()
                    continue
                elif diff > 0:
                    # Top of stack is larger; current asteroid explodes
                    break
                else:
                    # Both are equal size; both explode
                    stack.pop()
                    break
            else:
                # Runs only if the while loop did NOT break (current asteroid survived)
                stack.append(asteroid)
                
        return stack
