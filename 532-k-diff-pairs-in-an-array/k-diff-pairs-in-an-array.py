class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 0

        i = 0
        j = 1
        while j < n:
            if abs(nums[i] - nums[j]) < k:
                j += 1
            elif abs(nums[i] - nums[j]) > k:
                i += 1
            else:
                ans += 1
                i += 1
                j += 1

            while i > 0 and i < n and nums[i - 1] == nums[i]:
                i += 1
            while j > 0 and j < n and nums[j - 1] == nums[j]:
                j += 1
            if i == j:
                j += 1

        return ans