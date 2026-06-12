def bubble_sort(numbers: list[int]) -> None:
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(numbers) - 1):
            should_swap = numbers[i + 1] < numbers[i]
            if should_swap:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True
    return numbers


def main() -> None:
    numbers = [4, 2, 7, 1, 9, 6, 5, 8, 3]
    print("Unsorted list:", numbers)
    print("Sorted list:  ", bubble_sort(numbers))


if __name__ == "__main__":
    main()