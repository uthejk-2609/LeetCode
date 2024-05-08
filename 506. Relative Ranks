class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        max_score = max(score)
        total_ranks = [0]*(max_score+1)

        for i, sc in enumerate(score):
            total_ranks[sc] = i + 1

        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        ans = ['']*len(score)

        rank = 1
        for i in range(max_score, -1, -1):
            if total_ranks[i] != 0:
                if rank < 4:
                    ans[total_ranks[i] - 1] = ranks[rank - 1]
                else:
                    ans[total_ranks[i] - 1] = str(rank)
                rank += 1

        return ans
