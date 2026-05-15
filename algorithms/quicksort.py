def quicksort(numbers: list[int], low: int = 0, high: int | None = None) -> list[int]:
    if high is None:
        high = len(numbers) - 1
    if low >= high:
        return numbers
    pivot_index = _partition(numbers, low, high)
    quicksort(numbers, low, pivot_index - 1)
    quicksort(numbers, pivot_index + 1, high)
    return numbers


def _partition(numbers: list[int], low: int, high: int) -> int:
    pivot = numbers[high]
    i = low
    for j in range(low, high):
        if numbers[j] <= pivot:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            i += 1
    numbers[i], numbers[high] = numbers[high], numbers[i]
    return i


def main() -> None:
    numbers = [4, 2, 7, 1, 9, 6, 5, 8, 3]
    print("Unsorted:", numbers)
    print("Sorted:  ", quicksort(numbers))


if __name__ == "__main__":
    main()