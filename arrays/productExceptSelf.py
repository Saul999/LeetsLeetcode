# class Solution(object):
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         n = len(nums)
#         pre, post = [1] * n, [1]* n
#         sumPre = 1
#         sumPost = 1
#         final = [1] * n
#         print(len(pre),post)


#         for i in range(n):
#             final[i] *= sumPre
#             sumPre = sumPre * nums[i]

#         for i in range(len(nums)-1, -1, -1):
#             final[i] *= sumPost
#             sumPost = sumPost * nums[i]

#         # for i in range(n):
#         #     final[i]= pre[i] * post[i]

#         print(final)
#         print(pre)
#         print(post)
#         return final

#final answer 7/08/24
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        final = [1] * (len(nums))
        product = 1
        for i in range(len(nums)):
            final[i] = product
            product = nums[i] * product 
        product2 = 1
        for i in range(len(nums) -1, -1,-1):
            final[i] = product2 * final[i]
            product2 = nums[i] * product2

        return final

        
            
        

        