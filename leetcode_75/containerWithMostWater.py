class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right:
            if min(height[left], height[right]) * (right - left) > maxArea:
                maxArea = min(height[left], height[right]) * (right - left)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxArea
    
height = [1,1]
sol = Solution()
print(sol.maxArea(height))
        