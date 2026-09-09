class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for ix, i in enumerate(nums):
            if target - i in nums[0:ix]+nums[ix+1:]:
                for jx, j in enumerate(nums):
                    if ix != jx and j == target - i:
                        return [ix, jx]
            else:
                continue
        return result