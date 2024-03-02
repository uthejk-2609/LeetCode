def missingNumber(nums):
    nums = sorted(nums)
    i = 0
    
    for num in nums:
        if i != num:
            return i
        i = i + 1
