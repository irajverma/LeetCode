class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = dict()
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        for key, value in dic.items():
            if value > len(nums)/2:
                return key