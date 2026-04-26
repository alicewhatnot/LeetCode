class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        for _ in range(len(s) // 2):
            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")
        
        return s == ""

        