class Solution(object):
    def maxDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        seenChars = set()
        for char in s:
            if char not in seenChars:
                seenChars.add(char)

        return(len(seenChars))
