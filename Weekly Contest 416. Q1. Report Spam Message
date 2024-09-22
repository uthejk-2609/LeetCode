class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        count = 0
        bannedWords = set(bannedWords)

        for i in message:
            if i in bannedWords:
                count += 1

        return count > 1
