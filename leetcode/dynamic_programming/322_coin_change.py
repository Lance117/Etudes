class Solution:
    def coinChange(self, coins, amount):
        """
        use a table to keep track of min ways to make total. check table
        if complement of cur change was already recorded
        """
        count = [0] + [float('inf')] * amount
        for c in coins:
            for change in range(c, amount + 1):
                count[change] = min(count[change - c] + 1, count[change])
        return -1 if count[-1] == float('inf') else count[-1]
