class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        i = -1
        j = 0
        res = [0] * num_people
        while candies > 0:
            i += 1
            if i == num_people:
                i = 0
            j += 1
            candie = j if candies > j else candies
            candies -= j
            res[i] += candie
        return res