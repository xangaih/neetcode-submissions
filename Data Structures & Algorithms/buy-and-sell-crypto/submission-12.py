class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        res = 0

        for r in range(len(prices)):
            res = max(res, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l = r 
        
        return res
            
        