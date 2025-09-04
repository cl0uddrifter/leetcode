# Problem 334
# Run   O(n)
# Space O(1)

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        small = nums[0]
        medium = float('inf')

        for i in range(1, n):
            if nums[i] <= small:
                small = nums[i]
            elif nums[i] <= medium:
                medium = nums[i]
            else:
                return True

        return False
