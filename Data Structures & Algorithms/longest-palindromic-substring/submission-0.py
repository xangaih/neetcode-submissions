class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.best_st = 0
        self.best_len = 0

        def long(l, r):
                
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) >= self.best_len:
                    self.best_st = l
                    self.best_len = (r - l + 1)
                l = l - 1
                r = r + 1
            
        for n in range(len(s)):
            even =  long(n, n + 1)
            odd = long(n, n)
        
        return s[self.best_st:self.best_st + self.best_len]
        
       
                