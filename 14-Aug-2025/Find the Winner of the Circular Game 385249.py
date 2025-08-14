# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1, n + 1))
        return self._solve_recursively(friends, 0, k)

    def _solve_recursively(self, friends: list, start_index: int, k: int) -> int:
        if len(friends) == 1:
            return friends[0]
        else:
            index_to_remove = (start_index + k - 1) % len(friends)
            friends.pop(index_to_remove)
            new_start_index = index_to_remove
            return self._solve_recursively(friends, new_start_index, k)