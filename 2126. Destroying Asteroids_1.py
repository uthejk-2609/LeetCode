class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids = sorted(asteroids)
        curr_mass = mass
        n = len(asteroids)

        for i in range(n):
            if curr_mass < asteroids[i]:
                return False
            else:
                curr_mass += asteroids[i]
        
        return True
