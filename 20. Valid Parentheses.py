class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            else:
                if not stack:
                    return False
                if i == ')' and stack.pop() != '(':
                    return False
                if i == ']' and stack.pop() != '[':
                    return False
                if i == '}' and stack.pop() != '{':
                    return False
        return len(stack) == 0
