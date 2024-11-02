class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        min_dis = 10000
        index=-1
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                dist= abs(points[i][0]-x)+abs(points[i][1]-y)
                if dist<min_dis:
                    min_dis=dist
                    index=i
        return index