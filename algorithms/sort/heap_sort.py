def heap_sort(numbers: list[int]) -> list[int]:
    heap_size = len(numbers)
    for i in range(heap_size // 2 - 1, -1, -1):
        heapify(numbers, heap_size, i)
    for i in range(heap_size - 1, 0, -1):
        numbers[0], numbers[i] = numbers[i], numbers[0]
        heapify(numbers, i, 0)
    return numbers


def heapify(numbers: list[int], heap_size: int, root_index: int) -> None:
    largest_index = root_index
    left_index = 2 * root_index + 1
    right_index = 2 * root_index + 2
    if left_index < heap_size and numbers[left_index] > numbers[largest_index]:
        largest_index = left_index
    if right_index < heap_size and numbers[right_index] > numbers[largest_index]:
        largest_index = right_index
    if largest_index != root_index:
        numbers[root_index], numbers[largest_index] = numbers[largest_index], numbers[root_index]
        heapify(numbers, heap_size, largest_index)


def main() -> None:
    numbers = [4, 2, 7, 1, 9, 6, 5, 8, 3]
    print("Unsorted list:", numbers)
    print("Sorted list:  ", heap_sort(numbers))


if __name__ == "__main__":
    main()