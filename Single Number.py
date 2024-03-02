def singleNumber(nums):
    l = len(nums)
    xorr = 0

    for i in range(0, l):
        xorr = xorr^nums[i]
    return xorr
