"""
Problem link: https://open.kattis.com/problems/pervasiveheartmonitor
Problem source: David Sturgill / Baylor Competitive Learning
"""

import sys

def main() -> None:
    for line in sys.stdin:
        customer_data = line.strip().split()
        if customer_data[0][0].isnumeric():
            measurement_sum, no_measurements = 0, 0
            customer_name = ""
            while customer_data[0][0].isnumeric():
                measurement_sum += float(customer_data.pop(0))
                no_measurements += 1
            measurements_average = measurement_sum/no_measurements
            customer_name += " ".join(customer_data)
        else:
            customer_name = []
            while not customer_data[0][0].isnumeric():
                    customer_name.append(customer_data.pop(0))
            customer_name = " ".join(customer_name)
            measurements_average = sum([float(i) for i in customer_data])/len(customer_data)
        print(f"{measurements_average:.6f} {customer_name}")

if __name__ == "__main__":
    main()