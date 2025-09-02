# Problem 724
# Run   O(n)
# Space O(1)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums)

        for i in range(len(nums)):
            leftSum += nums[i]

            if leftSum == rightSum:
                return i

            rightSum -= nums[i]

        return -1