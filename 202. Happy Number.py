class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        fastasfboiii = set()

        while True:
            sqr = 0
            for i in n:
                sqr+= int(i)**2
            n = str(sqr)
            if n in fastasfboiii:
                return False
            elif n=="1":
                return True
            else:
                fastasfboiii.add(n)
