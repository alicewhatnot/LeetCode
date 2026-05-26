class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    
        fullPass = False
        
        #while not fullPass:

        for outerint in range (len(nums)-1):
            fullPass = True
            for integer in range (len(nums)-1):
                if nums[integer] == val:
                    temp = nums[integer + 1]
                    nums[integer + 1] = nums[integer]
                    nums[integer] = temp
                    fullPass = False
            if fullPass: break 


        
        total = 0
        for count in range (len(nums)):
            if nums[count] == val:
                break
            else:
                total += 1

        return total
