class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        degreeArray = []
        for vertexList in matrix:
            elementTotal = 0
            for element in vertexList:
                elementTotal += element
            degreeArray.append(elementTotal)
        
        return degreeArray