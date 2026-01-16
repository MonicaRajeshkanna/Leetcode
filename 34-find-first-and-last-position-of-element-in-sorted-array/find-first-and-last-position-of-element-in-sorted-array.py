class Solution:
    def searchRange(self, nums, target):
        def findFirst():
            left, right = 0, len(nums) - 1
            pos = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    pos = mid
                    right = mid - 1   # keep searching left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return pos
        
        def findLast():
            left, right = 0, len(nums) - 1
            pos = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    pos = mid
                    left = mid + 1   # keep searching right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return pos
        
        return [findFirst(), findLast()]
