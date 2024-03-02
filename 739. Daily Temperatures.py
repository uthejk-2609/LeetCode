class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = []
    
        for i in range(0, n):
            for j in range(i+1, n):
                if temperatures[i] < temperatures[j]:
                    answer.append(j-i)
                    break
            else:
                answer.append(0)
        return answer
