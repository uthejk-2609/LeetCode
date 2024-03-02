def rotateArray(nums, k):
    nums[:] = nums[k+1:len(nums)] + nums[0:k+1]
    return nums
