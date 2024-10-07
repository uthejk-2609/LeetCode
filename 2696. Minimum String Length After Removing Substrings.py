class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for i in s:
            if not stack:
                stack.append(i)
                continue
            if i == "B" and stack[-1] == "A":
                stack.pop()
            elif i == "D" and stack[-1] == "C":
                stack.pop()
            else:
                stack.append(i)

        return len(stack)
