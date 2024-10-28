class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i, j = 0, n - 1

        while i < j:
            curr_sum = numbers[i] + numbers[j]

            if  curr_sum > target:
                j -= 1
            elif curr_sum < target:
                i += 1
            else:
                return [i+1, j+1]
