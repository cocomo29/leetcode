class Solution:
    def average(self, salary: List[int]) -> float:
        ls = sorted(salary)
        ls = ls[1:-1]

        return sum(ls)/(len(ls))
