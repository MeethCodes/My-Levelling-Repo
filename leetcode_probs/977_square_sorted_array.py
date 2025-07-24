from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i, val in enumerate(nums):
            nums[i] = val ** 2
        nums.sort()         




sol1 = Solution()
sol1.sortedSquares([-4,-2,1,-5,0])
