class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0 
        while left < len(nums):
            right = left + 1
            if nums[left] == 0:
                while right < len(nums):
                    if nums[right] != 0:
                        nums[left], nums[right] = nums[right], nums[left]
                        break
                    right += 1
            left += 1
        print(nums)

        """    
        Better approach:

        def moveZeroes(self, nums):
            lastNonZero = 0
            
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[lastNonZero] = nums[i]
                    lastNonZero += 1
            
            for i in range(lastNonZero, len(nums)):
                nums[i] = 0     
        """

nums = [0,1,0,3,12]
sol =Solution()
sol.moveZeroes(nums)