# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        net_shift = [0] * (n + 1)
        
        for left, right, direction in shifts:
            if direction == 1:
                net_shift[left] += 1
                if right + 1 < n:
                    net_shift[right + 1] -= 1
            else:
                net_shift[left] -= 1
                if right + 1 < n:
                    net_shift[right + 1] += 1

        for i in range(1, n):
            net_shift[i] += net_shift[i - 1]

        arr = [chr(97 + i) for i in range(26)]
        result = []
        for i in range(n):
            letter = ord(s[i]) - 97
            shift = net_shift[i]
            shifted = (letter + shift) % 26
            result.append(arr[shifted])

        return ''.join(result)
