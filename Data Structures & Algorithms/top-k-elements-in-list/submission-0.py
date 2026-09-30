class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        

        for i, num in enumerate(nums):
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        return sorted(hashmap, key=lambda x: hashmap[x], reverse=True)[:k]