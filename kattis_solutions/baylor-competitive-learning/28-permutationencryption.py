"""
Problem link: https://open.kattis.com/problems/permutationencryption
Problem source: Greg Hamerly / Baylor Competitive Learning
"""

import sys

def main() -> None:
    while True:
        key = sys.stdin.readline().strip()
        if key == "0":
            break
        key = list(map(int, key.split()))
        key_length = key.pop(0)
        message = list(sys.stdin.readline().strip())
        padding = (-len(message)) % key_length
        message.extend([" "] * padding)
        encrypted_message = ""
        for segment in range(0, len(message), key_length):
            for j in key:
                encrypted_message += message[segment + j - 1]
        print(f"'{encrypted_message}'")

if __name__ == "__main__":
    main()