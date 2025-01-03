class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        stack = []
        ans = 0

        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)


        for i in range(n - 1, 0, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                ans = max(ans, i - stack[-1])
                stack.pop()

        return ans