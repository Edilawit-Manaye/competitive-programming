# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        hoo = Counter(word)
        fequ = Counter(hoo.values())

        if len(fequ) == 1:
            if 1 in fequ.values() or 1 in fequ:
                return True
            else:
                return False

        elif len(fequ) == 2:

            minFreq = min(fequ.keys())
            maxFreq = max(fequ.keys())

            if minFreq == 1 and fequ[minFreq] == 1:
                return True
            if maxFreq - minFreq == 1 and fequ[maxFreq] == 1:
                return True

        return False
