class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}
        def dp(i, j, score, turn):
            if i >= j:
                return score[0] > score[1]
            if (i, j) in cache:
                return cache[(i, j)]
            i_add = score[turn] + piles[i]
            j_add = score[turn] + piles[j]
            choice_i = dp(i + 1, j, [i_add, score[1]], turn ^ 1)
            choice_j = dp(i, j - 1, [piles[i], j_add], turn ^ 1)
            cache[(i, j)] = choice_i or choice_j
            return choice_i or choice_j
        
        return dp(0, len(piles) - 1, [0, 0], 0)
