"""
Problem link: https://open.kattis.com/problems/continuousmedian
Problem source: Steven Halim / NUS Competitive Programming
"""

import sys
import heapq

def main() -> None:
    no_test_cases = int(sys.stdin.readline().strip())
    for _ in range(no_test_cases):
        no_items = int(sys.stdin.readline().strip())
        items = [int(s) for s in sys.stdin.readline().split()]
        low, high = [], []
        median_sum = 0
        for i in items:
            if not low or i <= -low[0]:
                heapq.heappush(low, -i)
            else:
                heapq.heappush(high, i)
            if len(low) < len(high):
                heapq.heappush(low, -heapq.heappop(high))
            elif len(low) > len(high) + 1:
                heapq.heappush(high, -heapq.heappop(low))
            if len(low) > len(high):
                median_sum += -low[0]
            else:
                median_sum += (-low[0] + high[0]) // 2
        print(median_sum)

if __name__ == "__main__":
    main()