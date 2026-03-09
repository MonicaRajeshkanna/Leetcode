class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0
        
        max_prod = min_prod = result = nums[0]
        
        for num in nums[1:]:
            temp_max = max(num, num * max_prod, num * min_prod)
            min_prod = min(num, num * max_prod, num * min_prod)
            max_prod = temp_max
            
            result = max(result, max_prod)
        
        return result