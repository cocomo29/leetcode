class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        maX = 0

        for i in strs:
            if i.isdigit():
                if maX < int(i):
                    maX = int(i)
            else:
                if maX < len(i):
                    maX = len(i)
                    
        return maX
