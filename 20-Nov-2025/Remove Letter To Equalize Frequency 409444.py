# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        hoo = Counter(word)
        feq = Counter(hoo.values())

        if len(feq) == 1:
            if 1 in feq.values() or 1 in feq:
                return True
            else:
                return False

        elif len(feq) == 2:

            minFreq = min(feq.keys())
            maxFreq = max(feq.keys())

            if minFreq == 1 and feq[minFreq] == 1:
                return True
            if maxFreq - minFreq == 1 and feq[maxFreq] == 1:
                return True

        return False
