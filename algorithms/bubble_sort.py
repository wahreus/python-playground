"""A bubble sort implementation with an animated demo."""


import os
import time


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def show_step(numbers: list[int], index: int, should_swap: bool) -> None:
    clear_screen()
    spacing = " " * (3 * index)
    print(numbers)
    print(spacing + " ^  ^")
    print(spacing + " swap" if should_swap else "")
    time.sleep(0.5)


def bubble_sort(numbers: list[int]) -> None:
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(numbers) - 1):
            should_swap = numbers[i + 1] < numbers[i]
            if should_swap:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
            show_step(numbers, i, should_swap)
    clear_screen()
    print(numbers)
    print("List sorted!\n")


def main() -> None:
    numbers = [4, 2, 7, 1, 9, 6, 5, 8, 3]
    bubble_sort(numbers)


if __name__ == "__main__":
    main()