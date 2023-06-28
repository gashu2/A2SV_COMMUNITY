class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        li_one = []
        li_two = []
        for i in s:
            li_one.append(i)
        for j in t:
            li_two.append(j)
        li_one.sort()
        li_two.sort()
        return(li_one == li_two)
        




            


