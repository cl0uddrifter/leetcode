# Problem 238
# Run   O(n)
# Space O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        products = [1] * n

        prefix = 1
        for i in range(n):
            products[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            products[i] *= suffix
            suffix *= nums[i]
        
        return products