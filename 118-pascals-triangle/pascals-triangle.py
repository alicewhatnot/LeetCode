class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
       # generate tree up to n
        tree = [[1]]

        currentlayer = 0
        for i in range(numRows-1):
            currentlayer += 1
            newlayer = []
            newlayer.append(1)
            for index in range(len(tree[currentlayer-1])-1):
                newlayer.append(tree[currentlayer-1][index]+tree[currentlayer-1][index+1])
            newlayer.append(1)
            tree.append(newlayer)

        return tree

