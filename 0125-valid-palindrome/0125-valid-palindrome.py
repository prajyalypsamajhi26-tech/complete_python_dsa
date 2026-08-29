class Solution:
    def isPalindrome(self, s: str) -> bool:
        final  =""
        s=s.lower()

        for ele in s:
           if ele.isalnum():
            final += ele


        return final==final[::-1]