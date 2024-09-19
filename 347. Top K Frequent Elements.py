class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans = []

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        freq_list = list(freq.items())
        freq_list.sort(key=lambda x: x[1], reverse = True)

        for i in freq_list[0:k]:
            ans.append(i[0])

        return ans   
