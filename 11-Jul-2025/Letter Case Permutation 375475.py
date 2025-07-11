# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result=[""]
        for c in s:
            temp=[] # temp resets in each iteration 
            if c.isalpha():
                for k in result:
                    temp.append(k+c.lower())
                    temp.append(k+c.upper())
            else:
                for k in result:
                    temp.append(k+c)
            result=temp
        return result

            

        
        