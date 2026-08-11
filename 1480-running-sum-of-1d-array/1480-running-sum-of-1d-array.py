class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        run = len(nums)
        ans=[]
        ans.append(nums[0])

        for i in range(1,run):
            x = ans[i-1]+ nums[i]
            ans.append(x)

        return ans