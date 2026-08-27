class Solution:
    def isPalindrome(self, s: str) -> bool:
        sirFinal = []
        s = s.lower()
        for element in s:
           if element.isalnum():
                sirFinal.append(element)
        
        return sirFinal==sirFinal[::-1]