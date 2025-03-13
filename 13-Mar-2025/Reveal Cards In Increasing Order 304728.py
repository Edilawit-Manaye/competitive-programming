# Problem: Reveal Cards In Increasing Order - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        queue = deque([i for i in range(len(deck))])
        ans = [0]* len(deck)
        for i in range(len(deck)):
            index = queue.popleft()
            ans[index] = deck[i]
            if queue:
                queue.append(queue.popleft())
        return ans
            
        