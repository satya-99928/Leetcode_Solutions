class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        low=prices[0]
        max_profit=0
        for price in prices:
            low=min(low,price)
            max_profit=max(max_profit,price-low)
        return max_profit
                
        