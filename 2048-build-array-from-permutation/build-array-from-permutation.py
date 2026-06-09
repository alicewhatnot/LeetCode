class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        for num in range(len(nums)):
            output.append(nums[nums[num]])
        return output