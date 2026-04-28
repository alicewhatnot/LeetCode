class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        reversechar = ""
        for i in range(len(str(n)) - 1, -1, -1):
            reversechar += str(n)[i]

        return abs(n - int(reversechar))