class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        i, j = 0, n-1

        while i < j:
            m = (i + j) // 2

            if arr[m] > arr[m+1]:
                j = m
            else:
                i = m + 1

        return i
