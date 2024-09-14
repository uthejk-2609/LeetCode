class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = int(len(arr)*0.05)
        arr =   arr[n:len(arr)-n]
        return sum(arr)/len(arr)
