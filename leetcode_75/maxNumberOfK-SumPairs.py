class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counts = dict()
        operations = 0
        for num in nums:
            complement = k - num
            if complement in counts and counts[complement] > 0:
                operations += 1
                counts[complement] -= 1
                if counts[complement] == 0:
                    del counts[complement]
            else:
                counts[num] = counts.get(num, 0) + 1
        return operations
            