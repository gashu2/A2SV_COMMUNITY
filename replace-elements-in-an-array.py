from typing import List

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        numSet = set(nums)
        numIndex = {num: index for index, num in enumerate(nums)}
        for oldValue, newValue in operations:
            if oldValue in numSet:
                index = numIndex[oldValue]
                nums[index] = newValue
                numSet.remove(oldValue)
                numSet.add(newValue)
                numIndex[newValue] = index
                del numIndex[oldValue]
        return nums
