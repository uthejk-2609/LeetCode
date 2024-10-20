class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ans = []
        curr = ""

        for char in target:
            curr += "a"
            ans.append(curr)

            while curr[-1] != char:
                curr = curr[:-1] + chr(((ord(curr[-1]) - ord('a') + 1) % 26) + ord('a'))
                ans.append(curr)

        return ans
