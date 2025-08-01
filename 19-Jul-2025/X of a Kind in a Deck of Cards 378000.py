# Problem: X of a Kind in a Deck of Cards - https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        frequencies = list(count.values())
        overall_gcd = reduce(gcd, frequencies)
        return overall_gcd > 1