class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0 
        right = 1
        maxSell = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxSell = max(maxSell, profit)
                
            else:
                left = right
                
            right += 1

        return maxSell
            
            
                
            

