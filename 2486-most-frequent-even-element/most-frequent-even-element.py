class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=Counter(nums)
        max=0
        m=-1
        for i,j in k.items():
            if i%2==0:
                if j>max:
                    m=i
                    max=j
                elif j==max:
                    m=min(m,i)
        return m
