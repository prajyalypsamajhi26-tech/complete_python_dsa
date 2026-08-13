class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        rev = 2

        for i in range(2,len(nums)):
            if nums[i] != nums[rev -2]:
                nums[rev] = nums[i]
                rev += 1
        return rev