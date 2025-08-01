class Solution(object):
    def minimumPerimeter(self, neededApples):
        """
        :type neededApples: int
        :rtype: int
        """
        sum =0
        l=0
        for l in range(100000):
            sum = 2 *l * (l+1)*((2*l)+1) 
            if sum >= neededApples:
                break
        return 8*l
                