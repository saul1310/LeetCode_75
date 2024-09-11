from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stable = []
        for i in asteroids:
            # If the asteroid is moving right or no possible collision, add it
            if i > 0:
                stable.append(i)
            else:
                # Handle left-moving asteroid
                while stable and stable[-1] > 0:
                    if stable[-1] < abs(i):  # Right-moving asteroid is smaller, destroy it
                        stable.pop()
                    elif stable[-1] == abs(i):  # Both asteroids are the same size, destroy both
                        stable.pop()
                        break
                    else:  # Right-moving asteroid is larger, the left-moving one is destroyed
                        break
                else:
                    # If no right-moving asteroid or stable is empty, add the left-moving asteroid
                    stable.append(i)
        
        return stable
