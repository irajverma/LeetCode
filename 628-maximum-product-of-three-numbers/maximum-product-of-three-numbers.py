class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max_product1 = nums[-1] * nums[-2] * nums[-3]        
        max_product2 = nums[0] * nums[1] * nums[-1]
        return max(max_product1, max_product2)