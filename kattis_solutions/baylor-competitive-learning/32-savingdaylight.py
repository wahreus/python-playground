"""
Problem link: https://open.kattis.com/problems/savingdaylight
Problem source: Greg Hamerly / Baylor Competitive Learning
"""

import sys

def main() -> None:
    lines = sys.stdin.readlines()
    for line in lines:
        month, day, year, sunrise, sunset = line.strip().split()
        sunrise_h, sunrise_m = map(int, sunrise.split(":"))
        sunset_h, sunset_m = map(int, sunset.split(":"))
        hours = sunset_h-sunrise_h
        minutes = sunset_m-sunrise_m
        if minutes < 0:
            hours -= 1
            minutes += 60
        print(month, day, year, hours, "hours", minutes, "minutes")

if __name__ == "__main__":
    main()