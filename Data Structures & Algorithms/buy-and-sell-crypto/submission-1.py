class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        output = 0 
        for idx in range(1, len(prices)):
            if prices[idx] - buy_price > output: 
                output = prices[idx] - buy_price
            if prices[idx] < buy_price:
                buy_price = prices[idx]
        return output 
