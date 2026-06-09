class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        for digit in str(n):
            total += int(digit)
        return total