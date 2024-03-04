class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens = sorted(tokens)
        n = len(tokens)
        l = 0
        r = n - 1
        score = 0
        max_score = 0

        while l <= r:
            if tokens[l] <= power:
                power = power - tokens[l]
                l = l + 1
                score = score + 1
            else:
                if score > 0:
                    power = power + tokens[r]
                    score = score - 1
                r = r - 1
            max_score = max(max_score, score)

        return max_score
