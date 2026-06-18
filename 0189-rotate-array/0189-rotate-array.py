class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n

        # Reverse whole array
        for i in range(n // 2):
            nums[i], nums[n - i - 1] = nums[n - i - 1], nums[i]

        # Reverse first k elements
        for i in range(k // 2):
            nums[i], nums[k - i - 1] = nums[k - i - 1], nums[i]

        # Reverse remaining elements
        for i in range((n - k) // 2):
            nums[k + i], nums[n - i - 1] = nums[n - i - 1], nums[k + i]