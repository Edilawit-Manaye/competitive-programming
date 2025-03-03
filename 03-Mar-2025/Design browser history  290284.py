# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/

class ListNode:
    def __init__(self, val: str, prev: 'ListNode' = None):
        self.val = val
        self.prev = prev
        self.next = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)

    def visit(self, url: str) -> None:
        new_node = ListNode(url, self.cur)
        self.cur.next = new_node
        self.cur = new_node

    def back(self, steps: int) -> str:
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    def forward(self, steps: int) -> str:
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val

