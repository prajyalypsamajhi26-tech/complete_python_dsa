class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)

        start = 0

        for i in range(n):
            if nums[i] != 0:
                nums[start], nums[i] = nums[i] , nums[start]

                start +=1