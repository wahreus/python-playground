"""
Problem link: https://open.kattis.com/problems/engineeringenglish
Problem source: Greg Hamerly / Baylor Competitive Learning
"""

import sys

def main() -> None:
    seen_words = set()
    for line in sys.stdin.readlines():
        line = line.strip().split()
        output = ""
        for word in line:
            word_lower = word.lower()
            if word_lower in seen_words:
                output += ". "
            else:
                seen_words.add(word_lower)
                output += f"{word} " 
        print(output.strip())

if __name__ == "__main__":
    main()