import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        
        heap = []
        for char, count in freq.items():
            heapq.heappush(heap, (-count, char))
        
        result = []
        prev_count, prev_char = 0, ''
        
        while heap:
            count, char = heapq.heappop(heap)
            
            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))
            
            result.append(char)
            
            prev_count, prev_char = count + 1, char
        
        result_str = ''.join(result)
        if len(result_str) == len(s):
            return result_str
        else:
            return ""
