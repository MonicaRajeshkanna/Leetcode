class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                # Min is in right half
                left = mid + 1
            else:
                # Min is in left half including mid
                right = mid
        
        return nums[left]