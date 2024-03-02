class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        result = []
        
        for i in range(0, len(pattern) + 1):
            if i == len(pattern) or pattern[i] == 'I':
                stack.append(i + 1)
                while stack:
                    result.append(stack.pop())
            else:
                stack.append(i + 1)

        return ''.join(map(str, result))
