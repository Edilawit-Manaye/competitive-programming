# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        g = defaultdict(list)
        indegree = [0] * len(quiet)
        res = list(range(len(quiet)))

        for a, b in richer:
            g[a].append(b)
            indegree[b] += 1

        q = deque([i for i, v in enumerate(indegree) if v == 0])

        while q:
            node = q.popleft()
            for nei in g[node]:
                if quiet[res[node]] < quiet[res[nei]]:
                    res[nei] = res[node]
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return res