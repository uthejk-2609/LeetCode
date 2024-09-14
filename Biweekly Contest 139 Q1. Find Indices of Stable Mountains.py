class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        arr = []

        for i in range(len(height)-1):
            if height[i] > threshold:
                arr.append(i+1)

        return arr
