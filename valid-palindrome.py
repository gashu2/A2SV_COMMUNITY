class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")  
        s = s.strip()
        s = s.lower()
        string = ''
        for i in s:
            if i.isalnum():
                string += i
            else:
                continue
        return string == string[::-1]
