def maxArea(height):
    n = len(height)
    area = []
    
    for i in range(0, n):
        for j in range(i+1, n):
            h = min(height[i], height[j])
            w = j - i
            curr_area = h*w
            area.append(curr_area)
    return max(area)
