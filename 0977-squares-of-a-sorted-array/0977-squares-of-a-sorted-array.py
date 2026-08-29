class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) -1

        ans = [0] * len(nums)
        pos = len(nums) -1

        while left <= right:

            if abs(nums[left]) > abs(nums[right]): 
                ans[pos] = nums[left] **2
                left += 1

            else:
                ans[pos] = nums[right] **2
                right -=1

            pos -=1

        return ans