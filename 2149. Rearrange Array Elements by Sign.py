def rearrangeArray(nums):
    pos = []
    neg = []
    arr = []
    
    for num in nums:
        if num > 0:
            pos.append(num)
        else:
            neg.append(num)
    
    pos.extend(neg)
    n = len(pos)
    
    i = 0
    j = n // 2
    
    while j < n:
        arr.append(pos[i])
        arr.append(pos[j])
        
        i = i + 1
        j = j + 1
        
    return arr
