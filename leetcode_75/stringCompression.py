class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        left = 0
        right = 0
        while left < len(chars):
            if right >= len(chars) or chars[left] != chars[right]:
                chars[left + 1: right] = [] if right - left <= 1 else list(str(right- left))
                left += 1 if right - left <= 1 else len(str(right- left)) + 1 
                right = left
            right += 1
        print(chars)
        return len(chars)
            

    