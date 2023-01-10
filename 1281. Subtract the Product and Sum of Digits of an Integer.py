class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = str(n)
        sum = 0
        product = 1

        for i in n:
            sum += int(i)
            product *= int(i)
            
        return product - sum
