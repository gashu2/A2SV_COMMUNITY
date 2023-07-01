class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        stmt_list = ''
        for i in range(len(s)):
            if i in spaces:
                stmt_list += ' '
            stmt_list += s[i]
        return stmt_list
sol1 = Solution()
print(sol1.addSpaces("LeetcodeHelpsMeLearn", [8,13,15]))
