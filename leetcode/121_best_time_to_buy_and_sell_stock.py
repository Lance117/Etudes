def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    res, min_price = 0, float('inf')
    for p in prices:
        min_price = min(min_price, p)
        res = max(res, p - min_price)
    return res
