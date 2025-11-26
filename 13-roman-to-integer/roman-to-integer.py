class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
    
        numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        prev = 0
        for i in range (len(s) -1, -1, -1):
            char = s[i]
            current = numerals[char]
            if prev > current:
                total -= numerals[char]
            else:
                total += numerals[char]
            prev = numerals[char]
        return total


