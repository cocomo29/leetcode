class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sett = set()

        for i in nums:
            if nums.count(i) == 1:
                sett.add(i)

        return sum(sett)
