class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        stmt_list = []
        prev = 0
        for space in spaces:
            stmt_list.append(s[prev:space] + ' ')
            prev = space
        stmt_list.append(s[prev:])
        return ''.join(stmt_list)
sol1 = Solution()
print(sol1.addSpaces("spacing", [0, 1, 2, 3, 4, 5, 6]))
