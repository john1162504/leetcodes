class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        Input: nums = [2,1,5,0,4,6]
        Output: true
        """
        min_val = nums[0]
        mid_val = float("inf")
        for i in range(1, len(nums)):
            if nums[i] < min_val:
                min_val = nums[i]
                mid_val = float("inf")
                continue
            if nums[i] == min_val:
                continue
            if nums[i] < mid_val:
                mid_val = nums[i]
                continue
            if nums[i] > mid_val > min_val:
                return True
            
        return False

print(Solution.increasingTriplet(None, [1,2,1,3]))