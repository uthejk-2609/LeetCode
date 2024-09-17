class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word_s1 = s1.split(' ')
        word_s2 = s2.split(' ')
        words = word_s1 + word_s2

        count = Counter(words)
        res = []

        for s, cnt in count.items():
            if cnt == 1:
                res.append(s)

        return res
