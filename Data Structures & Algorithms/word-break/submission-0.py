class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hashmap = {}


        def helper(i):
            if i >= len(s):
                return True
            if i in hashmap:
                return hashmap[i]
            for w in wordDict:
                if w == s[i : i + len(w)]:
                    if helper(i + len(w)):
                        hashmap[i] = True
                        return True
            hashmap[i] = False
            return False
        
        return helper(0)


        