class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_check = {}
        for val in nums:
            if val in dup_check:
                return True
            else:
                dup_check[val] = 1
        return False