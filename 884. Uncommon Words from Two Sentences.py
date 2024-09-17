class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = s1.split(' ')
        words2 = s2.split(' ')
        words = words1 + words2
        word_count = {}

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        res = []

        for word in word_count:
            if word_count[word] == 1:
                res.append(word)

        return res
