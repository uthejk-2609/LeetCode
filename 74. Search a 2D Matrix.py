class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary Search
        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = rows * cols - 1

        while low <= high:
            mid = (low + high) // 2
            midValue = matrix[mid//cols][mid%cols]

            if midValue == target:
                return True
            elif midValue > target:
                high = mid - 1
            elif midValue < target:
                low = mid + 1
        
        return False
