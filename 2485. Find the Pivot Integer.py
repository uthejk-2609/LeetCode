class Solution:
    def pivotInteger(self, n: int) -> int:
        arr = []
        for i in range(0, n+1):
            arr.append(i)

        j = 1
        while sum(arr[0:j+1]) != sum(arr[j:len(arr)+1]):
            if j < len(arr)+1:
                j = j + 1
            else:
                return -1
        
        return j
