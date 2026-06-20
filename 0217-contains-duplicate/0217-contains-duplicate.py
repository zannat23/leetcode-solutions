class Solution(object):
    def containsDuplicate(self, nums):

        mp = {}

        for num in nums:
            if num in mp:
                return True
            mp[num] = 1

        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
