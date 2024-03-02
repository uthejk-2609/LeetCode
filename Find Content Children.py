def findContentChildren(g, s) -> int:
        g = sorted(g)
        s = sorted(s)
        n1 = len(g)
        n2 = len(s)
        count = 0
        i = 0
        j = 0

        while i<n1 and j<n2:
            if s[j] >= g[i]:
                count = count + 1
                i = i + 1
                j = j + 1
            else:
                j = j + 1
                
        return count
