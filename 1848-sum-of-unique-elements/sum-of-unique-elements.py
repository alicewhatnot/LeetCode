class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        unique = set()
        elementsSubtracted = set()
        for num in nums:
            if num in unique:
                if num not in elementsSubtracted:
                    total -= num
                    elementsSubtracted.add(num)
            else:
                total += num
            unique.add(num)
        return total