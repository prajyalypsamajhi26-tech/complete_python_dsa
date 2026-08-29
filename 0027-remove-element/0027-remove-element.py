class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)

        start =0
        for i in range(n):
            if nums[i] != val :
                nums[start] = nums[i]
                start += 1
                
        return start 