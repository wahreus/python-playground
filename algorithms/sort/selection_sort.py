def selection_sort(numbers: list[int]) -> list[int]:
    for i in range(len(numbers) - 1):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers


def main() -> None:
    numbers = [4, 2, 7, 1, 9, 6, 5, 8, 3]
    print("Unsorted list:", numbers)
    print("Sorted list:  ", selection_sort(numbers))


if __name__ == "__main__":
    main()