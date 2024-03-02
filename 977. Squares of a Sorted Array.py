class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq_arr = []

        for num in nums:
            sq = num*num
            sq_arr.append(sq)

        return sorted(sq_arr)
