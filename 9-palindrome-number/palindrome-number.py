class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

     
        flag = True
        for char in range(len(str(x))):
            if str(x)[char] != str(x)[len(str(x)) - char - 1]:
                flag = False

        return flag
