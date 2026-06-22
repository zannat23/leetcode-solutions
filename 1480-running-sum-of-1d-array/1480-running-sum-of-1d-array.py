class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
 
        result = [nums[0]]

        for i in range(1, len(nums)):
            result.append(result[-1] + nums[i])

        return result