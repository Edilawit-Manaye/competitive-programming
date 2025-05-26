# Problem: Decode XORed Array - https://leetcode.com/problems/decode-xored-array/description/

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result=[first]
        for num in encoded:
            result.append(num^first)
            first=result[-1]
        return result 

        