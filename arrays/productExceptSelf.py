class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        pre, post = [1] * n, [1]* n
        sumPre = 1
        sumPost = 1
        final = [1] * n
        print(len(pre),post)


        for i in range(n):
            pre[i] = sumPre
            sumPre = sumPre * nums[i]

        for i in reversed(range(n)):
            post[i]= sumPost
            sumPost = sumPost * nums[i]
            final[i] = pre[i] * post[i]

        # for i in range(n):
        #     final[i]= pre[i] * post[i]

        print(final)
        print(pre)
        print(post)
        return final

        
            
        

        