class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<3:
            return -1
        n = len(nums)
        for i in range(n-1):
            min=i
            for j in range(i+1,n):
                if nums[j]<nums[min]:
                    min = j
            nums[i],nums[min]=nums[min],nums[i]
        first=nums[0]
        second =  nums[n-1]
        for i in range(1,n-1):
            if nums[i]!=first and nums[i] !=second:
                return nums[i]
        return -1