# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
      output=[] 
      row11=set("qwertyuiop",)
      row2=set("asdfghjkl")
      row3=set("zxcvbnm") 
      for word in words:
        newWord=set(word.lower())
        if newWord.issubset(row11) or newWord.issubset(row2) or newWord.issubset(row3):
            output.append(word)
      return output
