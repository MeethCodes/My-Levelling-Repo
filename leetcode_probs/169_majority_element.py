from collections import defaultdict
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ocr = defaultdict(int)
        for val in nums:
            ocr[val] += 1
        
        return max(ocr,key=ocr.get)


sol1 = Solution()

print(sol1.majorityElement([3,2,3]))