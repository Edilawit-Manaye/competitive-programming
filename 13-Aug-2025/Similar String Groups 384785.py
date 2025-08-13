# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        N = len(strs)
        done = [False] * N
        def go(index):
            for i in range(N):
                if not done[i]:
                    delta = 0
                    for a, b in zip(strs[index], strs[i]):
                        if a != b:
                            delta += 1
                        if delta > 2:
                            break
                    else:
                        done[i] = True
                        go(i)

        count = 0
        for i in range(N):
            if not done[i]:
                count += 1
                done[i] = True
                go(i)

        return count