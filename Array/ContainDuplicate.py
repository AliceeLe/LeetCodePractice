# Problem: https://neetcode.io/problems/duplicate-integer

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lenList = len(nums)
        lenSet = len(set(nums))
        return not (lenList == lenSet)