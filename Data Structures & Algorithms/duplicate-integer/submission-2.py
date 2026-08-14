class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
        


