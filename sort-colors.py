class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n = len(nums)
        for i in range(n):
            for j in range(0,n-i-1):
                if nums[j+1] < nums[j]:
                    nums[j+1], nums[j] = nums[j], nums[j+1]
        return(nums)
