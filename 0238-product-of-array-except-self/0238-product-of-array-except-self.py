class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [1] * n
        preProduct = 1
        for i in range(n):
            ans[i] = preProduct
            preProduct = preProduct * nums[i]

        postProduct = 1
        for i in range(n-1 , -1 , -1 ):
            ans[i] *= postProduct
            postProduct = postProduct * nums[i]

        return ans
