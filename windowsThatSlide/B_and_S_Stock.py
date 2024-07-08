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

# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         max_val = 0

#         l, r = 0, 1
        
#         while r <= len(prices) - 1:
#             if prices[r] < prices[l]:
#                 l = r
#                 r += 1
#             else:
#                 val = prices[r] - prices[l]
#                 max_val = max(max_val, val)
#                 r += 1
#         return max_val            


                
            


            
            
                
            

