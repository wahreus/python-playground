"""
Problem link: https://open.kattis.com/problems/musicalnotation
Problem source: Greg Hamerly / Baylor Competitive Learning
"""

import sys

def main() -> None:
    n = int(sys.stdin.readline().strip())
    staff = {note: f"{note}: " for note in "GFEDCBAgfedcba"}
    lined_notes = {"a", "e", "g", "B", "D", "F"}
    notes = sys.stdin.readline().strip().split()
    for note in notes:
        if len(note) > 1:
            note_length = int(note[1:])
            note = note[0]
        else:
            note_length = 1        
        for staff_note in staff:
            line = "-" if staff_note in lined_notes else " "
            marker = "*" if staff_note == note else line
            staff[staff_note] += marker * note_length + line
    for value in staff.values():
        print(*value[:-1], sep="")

if __name__ == "__main__":
    main()