class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1

        maxprofit = 0



        for r in range(len(prices)):
            maxprofit = max((prices[r] - prices[l]), maxprofit)

            if prices[r] < prices[l]:
                l = r
            
            
        
        return maxprofit