def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    midpoint = len(numbers) // 2
    left = merge_sort(numbers[:midpoint])
    right = merge_sort(numbers[midpoint:])
    return merge(left, right)


def merge(left, right):
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def main() -> None:
    numbers = [4, 2, 7, 1, 9, 6, 5, 8, 3]
    print("Unsorted list:", numbers)
    print("Sorted list:  ", merge_sort(numbers))


if __name__ == "__main__":
    main()