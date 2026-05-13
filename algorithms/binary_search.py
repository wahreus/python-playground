"""An interactive binary search implementation."""


def binary_search(numbers: list[int], target: int) -> int | None:
    """Return the index of target in a sorted list, or None if not found."""
    left = 0
    right = len(numbers) - 1
    while left <= right:
        middle = (left + right) // 2
        if numbers[middle] == target:
            return middle
        if target > numbers[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return None


def get_integer_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def main() -> None:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Sorted list:", *numbers)

    target = get_integer_input("Enter item to find: ")
    index_found = binary_search(numbers, target)

    if index_found is not None:
        print(f"Item was found at index {index_found}.")
    else:
        print("Item was not found in the list.")


if __name__ == "__main__":
    main()