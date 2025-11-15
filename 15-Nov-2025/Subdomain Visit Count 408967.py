# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cp = defaultdict(int)

        for cpdomain in cpdomains:
            x, y = cpdomain.split()
            x = int(x)
            subdomains = y.split('.')
            for i in range(len(subdomains)):
                cp['.'.join(subdomains[i:])] += x
        return [f"{x} {y}" for y, x in cp.items()]