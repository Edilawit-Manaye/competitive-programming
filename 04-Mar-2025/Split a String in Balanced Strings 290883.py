# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l_counter,r_counter,counter=0,0,0
        for i in range(len(s)):
            if s[i]=="R":
                r_counter+=1
            elif s[i]=="L":
                l_counter+=1
            if r_counter==l_counter:
                counter+=1
        return counter 
        