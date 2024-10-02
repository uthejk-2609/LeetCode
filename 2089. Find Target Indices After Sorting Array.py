class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_arr = sorted(nums)
        n = len(nums)
        res = []
        
        for i in range(n):
            if sorted_arr[i] == target:
                res.append(i)

        return res
