class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = {}
        for val in nums:
            if val in dups:
                return True
            dups[val] = val
        return False