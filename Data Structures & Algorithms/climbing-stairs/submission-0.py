class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def ways(k):
            # base cases
            if k == 1:
                return k
            if k == 2:
                return k

            # already in the notebook?
            if k in memo:
                return memo[k]

            # not there yet: compute it, write it down, return it
            memo[k] = ways(k-1) + ways(k - 2) 
            return memo[k]

        return ways(n)
        
        