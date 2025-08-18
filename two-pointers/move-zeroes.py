# Problem 283
# Run   O(n)
# Space O(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """  
        n0 = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[n0]
                nums[n0] = nums[i]
                nums[i] = temp
                n0 += 1
