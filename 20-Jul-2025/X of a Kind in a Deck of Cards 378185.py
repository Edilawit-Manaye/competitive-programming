# Problem: X of a Kind in a Deck of Cards - https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
       c=Counter(deck)
       freq=list(c.values())
       x=reduce(gcd,freq)
       return x >1 