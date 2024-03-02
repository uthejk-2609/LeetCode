class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        nums = sorted(nums)
        arr = []

        for i in range(0, l-2):

            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            j = i + 1
            k = l - 1

            while j < k:
                
                if nums[i] + nums[j] + nums[k] == 0:
                    a = [nums[i], nums[j], nums[k]]
                    arr.append(a)

                    while j < k and nums[j] == nums[j+1]:
                        j = j + 1

                    while j < k and nums[k] == nums[k-1]:
                        k = k - 1

                    j = j + 1
                    k = k - 1

                elif nums[i] + nums[j] + nums[k] < 0:
                    j = j + 1

                else:
                    k = k - 1

        return arr
