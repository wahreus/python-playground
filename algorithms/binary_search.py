def binary_search(numbers: list[int], target: int) -> int | None:
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


def main() -> None:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 7
    print("Sorted list: ", numbers)
    print("Target item: ", target)
    found = binary_search(numbers, target)
    if found is not None:
        print(f"- Item {target} was found at index {found}.")
    else:
        print(f"- Item {target} was not found.")   


if __name__ == "__main__":
    main()