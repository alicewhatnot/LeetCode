class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        returnNums = nums
        for i in range (len(nums)-1, -1, -1):
            returnNums.append(nums[i])

        return returnNums