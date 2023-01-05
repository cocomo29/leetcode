class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}

        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1

        value = [i for i in dic if dic[i]==1]
        return(value[0])
