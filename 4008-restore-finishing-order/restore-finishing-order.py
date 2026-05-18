class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        
        output = []
        for place in order:
            if place in friends:
                output.append(place)

        return output