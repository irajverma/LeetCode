class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for num in nums:
            sum += num
        
        lsum = 0
        
        for i in range(len(nums)):

            rsum = sum - lsum - nums[i]
            
            if lsum == rsum:
                return i
            
            lsum += nums[i]

        return -1