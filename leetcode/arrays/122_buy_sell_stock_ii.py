class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        f([[7,1,5,3,6,4]]) -> 7
        cache -> [0,0,4,4,7,7]
        c[i] = c[i - 1] + max(p[i]-buy_price, 0) -> new_buy_p = p[i]
        if p[i] < buy_price, p[i] is new buy price
        f([1,2,3,4,5]) -> 4
        f([3,2,1]) -> 0
        
        buy_p = prices[0]
        c = [0] * len(prices)
        if len(prices) < 2:
            return 0
        for i in range(1, len(prices)):
            cur = prices[i]
            profit = cur - buy_p
            c[i] = c[i - 1] + max(profit, 0)
            if profit > 0 or cur < buy_p:
                buy_p = cur
        return c[-1]
        """
        profit = 0
        if len(prices) < 2:
            return 0
        for i in range(1, len(prices)):
            cur_profit = prices[i] - prices[i - 1]
            if cur_profit > 0:
                profit += cur_profit
        return profit
