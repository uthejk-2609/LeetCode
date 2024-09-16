class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrow = 1
        xstart = points[0][0]
        xend = points[0][1]
        n = len(points)

        for i in range(1, n):
            if points[i][0] <= xend:
                xstart = max(xstart, points[i][0])
                xend = min(xend, points[i][1])
            else:
                arrow = arrow + 1
                xstart = points[i][0]
                xend = points[i][1]

        return arrow
