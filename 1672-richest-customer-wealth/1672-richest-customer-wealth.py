class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans =0

        for accounts in accounts:
            ans = max(ans,sum(accounts))

        return ans