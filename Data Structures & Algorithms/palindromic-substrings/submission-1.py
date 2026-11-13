class Solution:
    def countSubstrings(self, s: str) -> int:
        self.res = 0

        def helper(l, r):
            
            while l >= 0 and r < len(s) and s[l] == s[r]:  
                self.res += 1
                l = l - 1
                r  = r + 1

            return self.res
        
        for n in range(len(s)):
            even = helper(n, n)
            odd = helper(n, n + 1)

        return self.res

        

        