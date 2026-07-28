"""
Problem link: https://open.kattis.com/problems/pachydermpeanutpacking
Problem source: Greg Hamerly / Baylor Competitive Learning
"""

import sys
from dataclasses import dataclass

@dataclass
class Box:
    x1: float
    y1: float
    x2: float
    y2: float
    peanut_type: str

    def contains(self, x: float, y: float) -> bool:
        return self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2

def main() -> None:
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            return
        boxes = []
        for _ in range(n):
            x1, y1, x2, y2, peanut_type = (sys.stdin.readline().split())
            boxes.append(Box(float(x1), float(y1), float(x2), float(y2), peanut_type))
        m = int(sys.stdin.readline())
        for _ in range(m):
            x, y, peanut_type = sys.stdin.readline().split()
            x = float(x)
            y = float(y)
            for box in boxes:
                if box.contains(x, y):
                    if peanut_type == box.peanut_type:
                        print(peanut_type, "correct")
                    else:
                        print(peanut_type, box.peanut_type)
                    break
            else:
                print(peanut_type, "floor")

if __name__ == "__main__":
    main()