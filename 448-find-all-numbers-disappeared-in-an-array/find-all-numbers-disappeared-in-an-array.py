class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            temp = abs(nums[i])
            nums[temp-1] = -(abs(nums[temp-1]))
        for i in range(len(nums)):
            if nums[i]>0:
                res.append(i+1)
        return res