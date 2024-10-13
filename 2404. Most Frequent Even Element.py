class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            if num % 2 == 0:
                if num not in freq:
                    freq[num] = 1
                else:
                    freq[num] += 1
        maxx = 0
        ans = -1

        for numm, count in freq.items():
            if count > maxx:
                maxx, ans = count, numm
            elif count == maxx:
                ans = min(numm, ans)

        return ans
