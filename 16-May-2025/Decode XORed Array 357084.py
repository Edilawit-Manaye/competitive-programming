# Problem: Decode XORed Array - https://leetcode.com/problems/decode-xored-array/description/

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res=[first]
        for num in encoded:
            res.append(num^first)
            first=res[-1]
        return res 

        