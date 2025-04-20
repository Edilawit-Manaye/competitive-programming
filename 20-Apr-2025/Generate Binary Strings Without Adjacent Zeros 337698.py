# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        def rec(temp):
            if len(temp) == n:
                ans.append("".join(temp[:]))
                return
            if not temp or temp[-1] == "1":
                temp.append("0")
                rec(temp)
                temp.pop()
            temp.append("1")
            rec(temp)
            temp.pop()
        rec([])
        return ans
            