class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        substring = []
        substringLengths = [0]
        for char in s:
            if char in substring:
                substringLengths.append(len(substring))
                while char in substring:
                    del substring[0]
                substring.append(char)
            else:
                substring.append(char)
       
        substringLengths.append(len(substring))

        return max(substringLengths)
