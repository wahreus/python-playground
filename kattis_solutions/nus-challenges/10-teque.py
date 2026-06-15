"""
Problem link: https://open.kattis.com/problems/teque
Problem source: Tan Jun An / NUS Competitive Programming
"""

import sys

class Teque:
    def __init__(self) -> None:
        self.left = {}
        self.right = {}
        self.left_min = 0
        self.left_max = 0
        self.right_min = 0
        self.right_max = 0
        self.left_len = 0
        self.right_len = 0
    def rebalance(self) -> None:
        if self.left_len > self.right_len + 1:
            self.left_max -= 1
            val = self.left.pop(self.left_max)
            self.left_len -= 1
            self.right_min -= 1
            self.right[self.right_min] = val
            self.right_len += 1
        elif self.left_len < self.right_len:
            val = self.right.pop(self.right_min)
            self.right_min += 1
            self.right_len -= 1
            self.left[self.left_max] = val
            self.left_max += 1
            self.left_len += 1
    def push_front(self, val: int) -> None:
        self.left_min -= 1
        self.left[self.left_min] = val
        self.left_len += 1
        self.rebalance()
    def push_back(self, val: int) -> None:
        self.right[self.right_max] = val
        self.right_max += 1
        self.right_len += 1
        self.rebalance()
    def push_middle(self, val: int) -> None:
        self.left[self.left_max] = val
        self.left_max += 1
        self.left_len += 1
        self.rebalance()
    def get(self, index: int) -> int:
        if index < self.left_len:
            return self.left[self.left_min + index]
        return self.right[self.right_min + index - self.left_len]
        
def main() -> None:
    n = int(sys.stdin.readline())
    q = Teque()
    output = []
    for _ in range(n):
        command, val = sys.stdin.readline().split()
        val = int(val)
        if command == "push_back":
            q.push_back(val)
        elif command == "push_front":
            q.push_front(val)
        elif command == "push_middle":
            q.push_middle(val)
        elif command == "get":
            output.append(str(q.get(val)))
    print("\n".join(output))

if __name__ == "__main__":
    main()