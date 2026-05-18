class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        s = set(friends)
        output = []
        for place in order:
            if place in s:
                output.append(place)

        return output