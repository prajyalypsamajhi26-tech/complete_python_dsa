class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0

        for i in range( len(nums)):
            temp = nums[i]
            c = 0

            while temp > 0:
                c += 1
                temp //= 10

            if c % 2 == 0:
                ans += 1

        return ans