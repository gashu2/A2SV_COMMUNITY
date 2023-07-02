class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        for i in range(n):
            counter = 0
            for j in range(n):
                if i != j and nums[j] < nums[i]:
                    counter += 1
            result.append(counter)        
        return result

