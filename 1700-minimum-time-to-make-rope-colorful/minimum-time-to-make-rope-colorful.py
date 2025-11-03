class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        colorArray = []
        time = 0

        for color in colors:
            colorArray.append(color)
        i = 0

        while i < (len(colorArray))-1:
            while i < len(colorArray) - 1 and colorArray[i] == colorArray[i + 1]:

                if neededTime[i] < neededTime[i + 1]:
                    time += neededTime[i]
                    colorArray.pop(i)
                    neededTime.pop(i)
                else:
                    time += neededTime[i+1]
                    colorArray.pop(i+1)
                    neededTime.pop(i+1)
            i += 1
        return time