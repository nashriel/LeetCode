class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if  n == 1:
            return 1
        if n == 2:
             return 2

        two_back = 1
        one_back = 2
        for i in range(2, n):
            next_num = two_back + one_back
            two_back = one_back
            one_back = next_num 
        return one_back