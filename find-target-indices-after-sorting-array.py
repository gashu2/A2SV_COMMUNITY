class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        indices = []
        counter = 0
        for i in nums:
            if i == target:
               indices.append(counter)
            counter += 1
        return(indices)

