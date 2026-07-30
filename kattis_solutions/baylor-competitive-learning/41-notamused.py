"""
Problem link: https://open.kattis.com/problems/notamused
Problem source: David Sturgill / Baylor Competitive Learning
"""

import sys
from collections import defaultdict

def main() -> None:
    day = 0
    entry_times = {}
    customer_costs = defaultdict(float)
    for line in sys.stdin:
        log_data = line.split()
        command = log_data[0]
        if command == "OPEN":
            day += 1
            entry_times = {}
            customer_costs = defaultdict(float)
        elif command == "CLOSE":
            print(f"Day {day}")
            for customer in sorted(customer_costs):
                print(f"{customer} ${customer_costs[customer]:.2f}")
            print()
        else:
            customer = log_data[1]
            time = int(log_data[2])
            if command == "ENTER":
                entry_times[customer] = time
            else:
                minutes = time - entry_times[customer]
                customer_costs[customer] += minutes * 0.1

if __name__ == "__main__":
    main()