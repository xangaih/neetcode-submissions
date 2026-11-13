class Solution:
    def numDecodings(self, s: str) -> int:
        self.res = {}

        def dfs(n):
            if n in self.res:
                return self.res[n]

            total = 0

            if n == len(s):
                return 1

            if s[n] == '0':
                return 0

            total = dfs(n + 1)
            if n + 1 < len(s):
                if 10 <= int(s[n : n + 2]) and int(s[n : n + 2]) <= 26:
                    total += dfs(n + 2)

            self.res[n] = total
            return total

        
        return dfs(0)





        